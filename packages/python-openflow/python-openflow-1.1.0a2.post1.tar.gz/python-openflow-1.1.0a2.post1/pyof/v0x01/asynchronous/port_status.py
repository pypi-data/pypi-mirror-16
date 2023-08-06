"""Defines an Error Message."""

# System imports
from enum import Enum

# Local source tree imports
from pyof.v0x01.common.header import Header, Type
from pyof.v0x01.common.phy_port import PhyPort
from pyof.v0x01.foundation.base import GenericMessage
from pyof.v0x01.foundation.basic_types import PAD, UBInt8

# Third-party imports

__all__ = ('PortStatus', 'PortReason')

# Enums


class PortReason(Enum):
    """What changed about the physical port."""

    #: The port was added
    OFPPR_ADD = 0
    #: The port was removed
    OFPPR_DELETE = 1
    #: Some attribute of the port has changed
    OFPPR_MODIFY = 2


# Classes

class PortStatus(GenericMessage):
    """A physical port has changed in the datapath."""

    #: :class:`~.header.Header`: OpenFlow Header
    header = Header(message_type=Type.OFPT_PORT_STATUS)
    reason = UBInt8(enum_ref=PortReason)
    #: Align to 32-bits.
    pad = PAD(7)
    desc = PhyPort()

    def __init__(self, xid=None, reason=None, desc=None):
        """Assign parameters to object attributes.

        Args:
            xid (int): Header's xid.
            reason (PortReason): Addition, deletion or modification.
            desc (PhyPort): Port description.
        """
        super().__init__(xid)
        self.reason = reason
        self.desc = desc
