import base64

base64_message = '0x38 0x39 0x20 0x35 0x30 0x20 0x37 0x30 0x20 0x34 0x38'
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)
