# Echo client program
import socket
import sys
from datetime import datetime
import time

if __name__ == '__main__':

    HOST = "192.168.1.90"
    PORT = 1080
    if len(sys.argv) < 2:
        exit()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        def sleep(mins : float):
            time.sleep(mins * 60)
        
        received = ""
        def send(val : str):
            byte_to_send = bytes(val, 'utf-8')
            s.send(byte_to_send)
            data = s.recv(1024)
            print(repr(data))
            received += repr(data)

        script = sys.argv[1]
        exec(script)

        with open("command_script_history.txt", "a") as logfile:
            text = 30 * "*" + '\n'
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            text += dt_string 
            text += '\n' + "script: " + sys.argv[1] + "\nresponses: " + received + "\n"
            logfile.write(text)
