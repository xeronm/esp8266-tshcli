from ..dtlv import dtlvmeta

namespace_id = 1

class Message:
    CONTROL    = 2
    CONFIG_GET = 3
    CONFIG_SET = 4
    CONFIG_SAVE = 5

class NS_Service(dtlvmeta.namespace):
    _name = 'Service'
    _namespace_id = namespace_id

class Service(dtlvmeta.objectAVP):
    _name = 'Service'
    _code = 100
    _namespace = NS_Service

class ServiceId(dtlvmeta.uint16):
    _name = 'Service-Id'
    _code = 101
    _namespace = NS_Service

class ServiceEnabled(dtlvmeta.uint8):
    _name = 'Service-Enabled'
    _code = 103
    _namespace = NS_Service

class ServiceState(dtlvmeta.uint8):
    _name = 'Service-State'
    _code = 104
    _namespace = NS_Service
    # ENUM
    STATE_STOPED = 0
    STATE_RUNNING = 1
    STATE_FAILED  = 2
    STATE_STOPING = 3
    STATE_STARTING = 4
