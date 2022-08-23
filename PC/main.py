from XmlProtocolParser import *
from SshProtocolSender import *

if __name__ == "__main__":
    xmlParser = XmlProtocolParser()
    sshSender = SshProtocolSender()

    commands = xmlParser.getCommands()
    # commands["read_temperature"]
    if sshSender.checkConnection():
        print(sshSender.execCommand("uptime"))
