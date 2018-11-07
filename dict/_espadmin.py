#!/usr/bin/python
# -*- coding: utf-8 -*-

import dtlvmeta

namespace_id = 3

class Message:
    FW_OTA_INIT   = 10
    FW_OTA_UPLOAD = 11
    RESTART       = 12
    FW_VERIFY     = 13
    FW_OTA_DONE   = 14

class NS_EspAdmin(dtlvmeta.namespace):
    _name = 'ESP-Admin'
    _namespace_id = namespace_id


class System(dtlvmeta.objectAVP):
    _name = 'System'
    _code = 102
    _namespace = NS_EspAdmin

class Wireless(dtlvmeta.objectAVP):
    _name = 'Wireless'
    _code = 103
    _namespace = NS_EspAdmin

class Firmware(dtlvmeta.objectAVP):
    _name = 'Firmware'
    _code = 104
    _namespace = NS_EspAdmin

class MemoryDB(dtlvmeta.objectAVP):
    _name = 'Memory-DB'
    _code = 105
    _namespace = NS_EspAdmin

class WiFiStation(dtlvmeta.objectAVP):
    _name = 'WIFI-Station'
    _code = 106
    _namespace = NS_EspAdmin

class WiFiSoftAP(dtlvmeta.objectAVP):
    _name = 'WIFI-Soft-AP'
    _code = 107
    _namespace = NS_EspAdmin

class SystemSDKVersion(dtlvmeta.char):
    _name = 'System-SDK-Version'
    _code = 111
    _namespace = NS_EspAdmin

class SystemUpTime(dtlvmeta.uint32):
    _name = 'System-Uptime'
    _code = 112
    _namespace = NS_EspAdmin

class SystemChipId(dtlvmeta.uint32):
    _name = 'System-Chip-ID'
    _code = 113
    _namespace = NS_EspAdmin

class SystemFlashId(dtlvmeta.uint32):
    _name = 'System-Flash-ID'
    _code = 114
    _namespace = NS_EspAdmin

class SystemCPUFreq(dtlvmeta.uint8):
    _name = 'System-CPU-Frequence'
    _code = 115
    _namespace = NS_EspAdmin

class SystemBootLoaderVersion(dtlvmeta.uint8):
    _name = 'System-Boot-Loader-Version'
    _code = 116
    _namespace = NS_EspAdmin

class SystemHeapFree(dtlvmeta.uint32):
    _name = 'Heap-Free-Size'
    _code = 117
    _namespace = NS_EspAdmin

class SystemResetReason(dtlvmeta.uint8):
    _name = 'System-Reset-Reason'
    _code = 118
    _namespace = NS_EspAdmin

class FW_UserBin(dtlvmeta.uint8):
    _name = 'FW-User-Bin'
    _code = 125
    _namespace = NS_EspAdmin

class FW_Address(dtlvmeta.ptr24):
    _name = 'FW-Address'
    _code = 126
    _namespace = NS_EspAdmin

class FW_SizeMap(dtlvmeta.uint8):
    _name = 'FW-Size-Map'
    _code = 127
    _namespace = NS_EspAdmin

class FW_BinSize(dtlvmeta.uint32):
    _name = 'FW-Bin-Size'
    _code = 128
    _namespace = NS_EspAdmin

class FW_ReleaseDate(dtlvmeta.date_time):
    _name = 'FW-Release-Date'
    _code = 129
    _namespace = NS_EspAdmin

class FW_Digest(dtlvmeta.octets):
    _name = 'FW-Digest'
    _code = 130
    _namespace = NS_EspAdmin

class FW_InitDigest(dtlvmeta.octets):
    _name = 'FW-Init-Digest'
    _code = 131
    _namespace = NS_EspAdmin

class FW_Info(dtlvmeta.octets):
    _name = 'FW-Info'
    _code = 132
    _namespace = NS_EspAdmin

class FW_UserDataAddress(dtlvmeta.ptr24):
    _name = 'FW-User-Data-Address'
    _code = 133
    _namespace = NS_EspAdmin

class FW_UserDataSize(dtlvmeta.uint32):
    _name = 'FW-User-Data-Size'
    _code = 134
    _namespace = NS_EspAdmin

class MDB_BlockSize(dtlvmeta.uint16):
    _name = 'MDB-Block-Size'
    _code = 135
    _namespace = NS_EspAdmin

class MDB_Class(dtlvmeta.objectAVP):
    _name = 'MDB-Class'
    _code = 136
    _namespace = NS_EspAdmin

class MDB_ClassName(dtlvmeta.char):
    _name = 'MDB-Class-Name'
    _code = 137
    _namespace = NS_EspAdmin

class MDB_ObjectCount(dtlvmeta.uint16):
    _name = 'MDB-Object-Count'
    _code = 138
    _namespace = NS_EspAdmin

class MDB_PageCount(dtlvmeta.uint16):
    _name = 'MDB-Page-Count'
    _code = 139
    _namespace = NS_EspAdmin

class MDB_BlockCount(dtlvmeta.uint16):
    _name = 'MDB-Block-Count'
    _code = 140
    _namespace = NS_EspAdmin

class MDB_FreeSlots(dtlvmeta.uint16):
    _name = 'MDB-Free-Slots'
    _code = 141
    _namespace = NS_EspAdmin

class MDB_FreeSize(dtlvmeta.uint16):
    _name = 'MDB-Free-Size'
    _code = 142
    _namespace = NS_EspAdmin

class WIFI_OpMode(dtlvmeta.uint8):
    _name = 'WiFi-Operation-Mode'
    _code = 145
    _namespace = NS_EspAdmin

class WIFI_SSID(dtlvmeta.char):
    _name = 'WiFi-SSID'
    _code = 146
    _namespace = NS_EspAdmin

class WIFI_Password(dtlvmeta.char):
    _name = 'WiFi-Password'
    _code = 147
    _namespace = NS_EspAdmin

class WIFI_AuthMode(dtlvmeta.uint8):
    _name = 'WiFi-Auth-Mode'
    _code = 148
    _namespace = NS_EspAdmin

class WIFI_SleepType(dtlvmeta.uint8):
    _name = 'WiFi-Sleep-Type'
    _code = 149
    _namespace = NS_EspAdmin

class WIFI_AutoConnect(dtlvmeta.uint8):
    _name = 'WiFi-Auto-Connect'
    _code = 150
    _namespace = NS_EspAdmin

class WIFI_ConnectStatus(dtlvmeta.uint8):
    _name = 'WiFi-Connect-Status'
    _code = 151
    _namespace = NS_EspAdmin

class OTA_BinState(dtlvmeta.uint8):
    _name = 'OTA-State'
    _code = 165
    _namespace = NS_EspAdmin

class OTA_BinData(dtlvmeta.octets):
    _name = 'OTA-Bin-Data'
    _code = 166
    _namespace = NS_EspAdmin

class OTA_CurrentAddr(dtlvmeta.ptr24):
    _name = 'OTA-Current-Addr'
    _code = 167
    _namespace = NS_EspAdmin
