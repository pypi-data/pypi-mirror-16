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

from mqspeak.data import Measurement

class DataCollector:
    """!
    """

    ## @var updateBuffers
    # List of UpdateBuffer objects.

    ## @var channelUpdateSupervisor
    # UpdateSupervisor object.

    def onNewData(self, dataIdentifier, data):
        """!
        Notify data collector when new data is available.

        @param dataIdentifier Data identification.
        @param data Payload.
        """
