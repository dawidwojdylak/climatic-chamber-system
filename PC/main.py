from XmlProtocolParser import *
from SshProtocolSender import *

if __name__ == "__main__":
    xmlParser = XmlProtocolParser()
    sshSender = SshProtocolSender()

    commands = xmlParser.getCommands()
    # commands["read_temperature"]
    # print(sshSender.execCommand("pwd; mkdir t123; ls; ls"))
    if sshSender.checkConnection():
        print(sshSender.execCommand("python3 .py arg"))
