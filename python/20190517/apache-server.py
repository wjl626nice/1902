import socket

sk = socket.socket()
sk.bind(('', 8080))
sk.listen()

conn, addr = sk.accept()

client_msg = conn.recv(1024)
print(client_msg.decode())
conn.send(b'aa')

conn.close()
sk.close()

