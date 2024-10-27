from ..dtlv import dtlvmeta

namespace_id = 7

class Message:
    GPIO_SET = 10

class NS_GPIO(dtlvmeta.namespace):
    _name = 'GPIO'
    _namespace_id = namespace_id

class Port(dtlvmeta.objectAVP):
    _name = 'GPIO-Port'
    _code = 101
    _namespace = NS_GPIO

class FunctionDefault(dtlvmeta.uint8):
    _name = 'GPIO-Function-Default'
    _code = 103
    _namespace = NS_GPIO

class FunctionSet(dtlvmeta.uint8):
    _name = 'GPIO-Function-Set'
    _code = 104
    _namespace = NS_GPIO

class PortInUse(dtlvmeta.uint8):
    _name = 'GPIO-Port-In-Use'
    _code = 105
    _namespace = NS_GPIO

class PortAvailable(dtlvmeta.uint8):
    _name = 'GPIO-Port-Available'
    _code = 106
    _namespace = NS_GPIO

class PortValue(dtlvmeta.uint8):
    _name = 'GPIO-Port-Value'
    _code = 107
    _namespace = NS_GPIO

class PortPulseUs(dtlvmeta.uint16):
    _name = 'GPIO-Port-Pulse-us'
    _code = 108
    _namespace = NS_GPIO

class PortPullup(dtlvmeta.uint16):
    _name = 'GPIO-Port-Pullup'
    _code = 109
    _namespace = NS_GPIO
