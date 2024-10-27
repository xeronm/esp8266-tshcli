import re

def block_offset(block, offset = '\t'):
    return re.sub('^(?m)', offset, block)

def string_split(s, split_size, split_char):
    return re.sub('(.{%s})' % split_size, r'\1'+split_char, s)

def unix2win(text):
    return re.sub('$(?m)', '\r\n', text)

def byte_to_hex(val):
    return hex(int(val) & 0xffffffff)[2:].rjust(2, '0')[-2:]

def word_to_hex(val):
    return hex(int(val) & 0xffffffff)[2:].rjust(4, '0')[-4:]

def b3_to_hex(val):
    return hex(int(val) & 0xffffffff)[2:].rjust(6, '0')[-6:]

def int_to_hex(val):
    return hex(int(val) & 0xffffffff)[2:].rjust(8, '0')[-8:]

def int64_to_hex(val):
    return hex(int(val) & 0xffffffffffffffff)[2:].rjust(16, '0')[-16:]

def hex_to_ipv4(val):
    return '%d.%d.%d.%d' % (int(val[0:2], 16), int(val[2:4], 16), int(val[4:6], 16), int(val[6:8], 16))

def hex_to_mac48(val):
    octets = [ val[i*2:i*2+2] for i in range(len(val)/2) ]
    return ':'.join(octets)

def ipv4_to_hex(val):
    octets = val.split('.')
    return '%02.x%02.x%02.x%02.x' % (int(octets[0]), int(octets[1]), int(octets[2]), int(octets[3]))

def mac48_to_hex(val):
    octets = val.split(':')
    return ''.join(octets)

def ipv6_to_hex(val):
    return re.sub(':', '', val)
