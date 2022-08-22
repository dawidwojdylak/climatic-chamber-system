# Echo client program
import socket

HOST = "192.168.1.90"
PORT = 1080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("test")
    s.connect((HOST, PORT))
    # s.sendall(b'Hello, world')
    # s.send("A0")
    # s.sendall(b'S1')
    s.send(b'T')
    data = s.recv(1024)
    print('Received', repr(data))