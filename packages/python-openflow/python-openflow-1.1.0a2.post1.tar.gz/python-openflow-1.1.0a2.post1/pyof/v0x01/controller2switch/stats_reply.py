"""Response the stat request packet from the controller."""

# System imports

# Third-party imports

# Local imports
from pyof.v0x01.common.header import Header, Type
from pyof.v0x01.controller2switch.common import StatsTypes
from pyof.v0x01.foundation.base import GenericMessage
from pyof.v0x01.foundation.basic_types import ConstantTypeList, UBInt16

__all__ = ('StatsReply',)

# Classes


class StatsReply(GenericMessage):
    """Class implements the response to the config request."""

    #: OpenFlow :class:`.Header`
    header = Header(message_type=Type.OFPT_STATS_REPLY)
    body_type = UBInt16(enum_ref=StatsTypes)
    flags = UBInt16()
    body = ConstantTypeList()

    def __init__(self, xid=None, body_type=None, flags=None, body=None):
        """The constructor just assings parameters to object attributes.

        Args:
            body_type (StatsTypes): One of the OFPST_* constants.
            flags (int): OFPSF_REQ_* flags (none yet defined).
            body (ConstantTypeList): Body of the request.
        """
        super().__init__(xid)
        self.body_type = body_type
        self.flags = flags
        self.body = [] if body is None else body
