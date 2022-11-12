from XmlProtocolParser import *
from SshProtocolSender import *

# TODO:
# - class diagram (look for desing patterns)
# - unit tests
# - when reading value read also description of argument
# - setting time value
# - prepare wrong argument handling
# - response handling

if __name__ == "__main__":
    xmlParser = XmlProtocolParser()
    commands = xmlParser.importCommandsFromXml()
    

    print(commands)
    for i in range(len(commands)):
        # print(commands[i].name ,commands[i].prepareRequest(), commands[i].request[0])
        if commands[i].name == 'set_humidity_gradient_up':
            commands[i].setValue(29.23)

    for i in range(len(commands)):
        print(commands[i].name ,commands[i].prepareRequest(), commands[i].request[0])

    # sshSender = SshProtocolSender()

    # commands = xmlParser.getCommands()
    # commands["read_temperature"]
    # print(sshSender.execCommand("pwd; mkdir t123; ls; ls"))
    # if sshSender.checkConnection():
        # print(sshSender.execCommand("python3 .py arg"))


    # importCommandsFromXml()
