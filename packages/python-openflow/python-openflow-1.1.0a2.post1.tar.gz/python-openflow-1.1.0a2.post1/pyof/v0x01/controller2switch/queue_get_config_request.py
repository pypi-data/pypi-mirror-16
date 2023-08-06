"""Query the switch for configured queues on a port."""

# System imports

# Third-party imports

# Local source tree imports
from pyof.v0x01.common.header import Header, Type
from pyof.v0x01.common.phy_port import Port
from pyof.v0x01.foundation.base import GenericMessage
from pyof.v0x01.foundation.basic_types import PAD, UBInt16

__all__ = ('QueueGetConfigRequest',)


class QueueGetConfigRequest(GenericMessage):
    """Query structure for configured queues on a port."""

    header = Header(message_type=Type.OFPT_GET_CONFIG_REQUEST)
    port = UBInt16(enum_ref=Port)
    #: Pad to 64-bits
    pad = PAD(2)

    def __init__(self, xid=None, port=None):
        """The constructor just assings parameters to object attributes.

        Args:
            xid (int): xid of OpenFlow header
            port (Port): Target port for the query
        """
        super().__init__(xid)
        self.port = port
