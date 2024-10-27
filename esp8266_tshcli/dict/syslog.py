from ..dtlv import dtlvmeta

namespace_id = 2

class Message:
    QUERY = 11

class NS_Syslog(dtlvmeta.namespace):
    _name = 'Syslog'
    _namespace_id = namespace_id

class LogEntry(dtlvmeta.objectAVP):
    _name = 'Log-Entry'
    _code = 101
    _namespace = NS_Syslog

class LogSeverity(dtlvmeta.uint8):
    _name = 'Log-Severity'
    _code = 102
    _namespace = NS_Syslog

    LOG_NONE = 0
    LOG_CRITICAL = 1
    LOG_ERROR = 2
    LOG_WARNING = 3
    LOG_INFO = 4
    LOG_DEBUG = 5

class LogMessage(dtlvmeta.char):
    _name = 'Entry-Message'
    _code = 103
    _namespace = NS_Syslog

class LogTimestamp(dtlvmeta.date_time):
    _name = 'Entry-Timestamp'
    _code = 104
    _namespace = NS_Syslog

class LogRecordNumber(dtlvmeta.uint16):
    _name = 'Entry-Record-Number'
    _code = 105
    _namespace = NS_Syslog

