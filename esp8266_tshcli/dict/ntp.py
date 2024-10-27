from ..dtlv import dtlvmeta

namespace_id = 6

class Message:
    SETDATE = 10

class NS_NTP(dtlvmeta.namespace):
    _name = 'NTP'
    _namespace_id = namespace_id

class QueryState(dtlvmeta.uint8):
    _name = 'Query-State'
    _code = 101
    _namespace = NS_NTP

class QueryStateTime(dtlvmeta.date_time):
    _name = 'Query-State-Time'
    _code = 102
    _namespace = NS_NTP

class PollInterval(dtlvmeta.uint16):
    _name = 'Poll-Interval'
    _code = 103
    _namespace = NS_NTP

class Peer(dtlvmeta.objectAVP):
    _name = 'Peer'
    _code = 104
    _namespace = NS_NTP

class PeerState(dtlvmeta.uint8):
    _name = 'Peer-State'
    _code = 105
    _namespace = NS_NTP

class Peer_RTT_Mean(dtlvmeta.uint32):
    _name = 'Peer-RTT-Mean'
    _code = 106
    _namespace = NS_NTP

class Peer_RTT_Variance(dtlvmeta.uint32):
    _name = 'Peer-RTT-Variance'
    _code = 107
    _namespace = NS_NTP

class Peer_RTT_Offset(dtlvmeta.uint32):
    _name = 'Peer-Offset'
    _code = 108
    _namespace = NS_NTP
