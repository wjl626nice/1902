import struct

print(struct.pack('i', 123), len(struct.pack('i', 123)))
print(struct.pack('i', 1234345), len(struct.pack('i', 1234345)))
print(struct.pack('i', 2025465434), len(struct.pack('i', 2025465434)))

print(struct.unpack('i', b'\xa9\xd5\x12\x00')[0], type(struct.unpack('i', b'\xa9\xd5\x12\x00')[0]))