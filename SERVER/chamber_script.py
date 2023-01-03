# Echo client program
import socket
import sys
from datetime import datetime

HOST = "192.168.1.90"
PORT = 1080
if len(sys.argv) < 2:
    exit()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.send(b'A0')
    byte_to_send = bytes(sys.argv[1], 'utf-8')
    s.send(byte_to_send)
    data = s.recv(1024)
    print(repr(data))

    with open("command_history.txt", "a") as logfile:
        text = 30 * "*" + '\n'
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        text += dt_string 
        text += '\n' + "command: " + sys.argv[1] + "\nresponse: " + repr(data) + "\n"
        logfile.write(text)
