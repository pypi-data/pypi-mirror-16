# Copyright (C) Ivo Slanina <ivo.slanina@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from mqreceive.data import DataIdentifier
import os
import paho.mqtt.client as mqtt
import socket
import sys
import threading

class BrokerThreadManager:
    """!
    Manage broker receiving threads
    """

    ## @var idManager
    # Object responsible for managing receiver IDs.

    ## @var clients
    # Iterable of of receiver client objects.

    ## @var isThreadsRunning
    # Keep track if receiver threads are running.

    def __init__(self, listenDescriptors, dataCollector):
        """!
        Initiate BrokerThreadManager oject.

        @param listenDescriptors Listen descriptor iterable object.
            @li broker: broker descriptor object
            @li subsriptionIterable:
        @param dataCollector DataCollector object.
        """
        self.idManager = BrokerReceiverIDManager()
        self.clients = [BrokerReceiver(self.idManager.createReceiverID(), x, dataCollector) for x in listenDescriptors]
        self.isThreadsRunning = False

    def start(self):
        """!
        Start all receiving threads.
        """
        if self.isThreadsRunning:
            raise ThreadManagerException("Broker threads are already running")
        self.isThreadsRunning = True
        for client in self.clients:
            threading.Thread(target = client).start()

    def stop(self):
        """!
        Stop all receving threads.
        """
        if not self.isThreadsRunning:
            raise ThreadManagerException("Broker threads are already stopped")
        self.isThreadsRunning = False
        for client in self.clients:
            client.stop()

class BaseBrokerReceiver:
    """!
    Dummy implementation of broker receiverr object.
    """

    def __call__(self):
        """!
        Start receiving thread.
        """
        self.__notImplemented()

    def stop(self):
        """!
        Stop receiving thread.
        """
        self.__notImplemented()

    def isRunning(self):
        """!
        Check if broker receiver thread is running.
        """
        self.__notImplemented()

    def __notImplemented(self):
        raise NotImplementedError("Override in sub-class.")

class BrokerReceiver(BaseBrokerReceiver):
    """!
    Broker receiving thread
    """

    ## @var clientID
    # Client identification.

    ## @var broker
    # Broker object.

    ## @var subsciption
    # Broker subscribtion.

    ## @var dataCollector
    # Data collector object.

    ## @var client
    # MQTT client object.


    def __init__(self, clientID, listenDescriptor, dataHandler):
        """!
        Initiate BrokerReceiver object.

        @param clientID
        @param listenDescriptor Set containing following fields: (broker, subscription).
            @li broker: broker descriptor object
            @li subscription:
        @param dataCollector Listener object to deliver received updates.
        """
        self.clientID = clientID
        self.broker, self.subsciption = listenDescriptor
        self.dataHandler = dataHandler
        self.client = mqtt.Client(client_id = str(self.clientID))
        self._registerCallbacks()
        if self.broker.isAuthenticationRequired():
            self.client.username_pw_set(self.broker.user, self.broker.password)

    def _registerCallbacks(self):
        self.client.on_connect = self.onConnect
        self.client.on_disconnect = self.onDisconnect
        self.client.on_message = self.onMessage
        self.client.on_subscribe = self.onSubscribe
        self.client.on_unsubscribe = self.onUnsubscribe
        self.client.on_log = self.onLog

    def __call__(self):
        """!
        Broker receiver thread code.
        """
        keepAliveInterval = 60
        self.client.connect(self.broker.host, self.broker.port, keepAliveInterval)
        self.client.loop_forever()

    def onConnect(self, client, userdata, flags, rc):
        """!
        The callback for when the client receives a CONNACK response from the server.

        @param client
        @param userdata
        @param flags
        @param rc
        """
        for sub in self.subsciption:
            (result, mid) = self.client.subscribe(sub)

    def onDisconnect(self, client, userdata, rc):
        """!
        Callback when client is disconnected.

        @param client
        @param userdata
        @param rc
        """

    def onMessage(self, client, userdata, msg):
        """!
        The callback for when a PUBLISH message is received from the server.

        @param client
        @param userdata
        @param msg
        """
        dataIdentifier = DataIdentifier(self.broker, msg.topic)
        self.dataHandler.onNewData(dataIdentifier, msg.payload)

    def onSubscribe(self, client, userdata, mid, granted_qos):
        """!
        Callback when client is subscribed to topic.

        @param client
        @param userdata
        @param mid
        @param granted_qos
        """

    def onUnsubscribe(self, client, userdata, mid):
        """!
        Callback when client is unsubscribed.

        @param client
        @param userdata
        @param mid
        """

    def onLog(self, client, userdata, level, buf):
        """!
        Logging messages.

        @param client
        @param userdata
        @param level
        @param buf
        """

    def stop(self):
        """!
        Stop receiver thread. Call this method to nicely end __call__() method.
        """
        self.client.disconnect()

class BrokerReceiverID:
    """!
    Broker receiver thread ID.
    """

    ## @var hostname
    # Machine hostname

    ## @var pid
    # Current process PID

    ## @var receiverID
    # Receiver thread ID.

    def __init__(self, hostname, pid, receiverID):
        """!
        Create broker receiver thread lient ID.

        @param hostname Machine hostname.
        @param pid Current PID.
        @param receiverID Receiving thread ID.
        """
        self.hostname = hostname
        self.pid = pid
        self.receiverID = receiverID

    def __str__(self):
        """!
        Convert BrokerReceiverID to string.

        @return String.
        """
        return "mqspeak-{}-{}-{}".format(self.hostname, self.pid, self.receiverID)

    def __repr__(self):
        """!
        Convert BrokerReceiverID to representation string.

        @return Representation string.
        """
        return "<{}>".format(self.__str__())

class BrokerReceiverIDManager:
    """!
    Manage receiver IDs.
    """

    ## @var hostname
    # Machine hostname

    ## @var pid
    # Current process PID

    ## @var receiverCounter
    # Keep track how many broker IDs were created.

    def __init__(self):
        """!
        Initiate BrokerReceiverIDManager object.
        """
        self.hostname = socket.gethostname()
        self.pid = os.getpid()
        self.receiverCounter = 0

    def createReceiverID(self):
        """!
        Create new receiver ID.

        @return Receiver ID.
        """
        _receiverID = self.receiverCounter
        self.receiverCounter += 1
        return BrokerReceiverID(self.hostname, self.pid, _receiverID)

class ThreadManagerException(Exception):
    """!
    Indicate BrokerThreadManager error.
    """
