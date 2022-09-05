from XmlProtocolParser import *
from SshProtocolSender import *
from Command import *

def importCommandsFromXml():
    xmlParser = XmlProtocolParser()
    commands = []
    root = xmlParser.root

    if root.tag == "commands":
                for child in root:
                    command = Command(child.attrib.get("name"))
                    
                    for grandChild in child:
                        if grandChild.tag == 'description':
                            command.fillDescription(grandChild.text)
                        
                        if grandChild.tag == 'request':
                            for arg in grandChild:
                                argument = Argument(arg.text, arg.attrib.get("type"),  
                                arg.attrib.get("descr"), arg.attrib.get("min"), 
                                arg.attrib.get("max"), arg.attrib.get("unit"))

                                command.fillRequest(argument)
                        if grandChild.tag == 'response':
                            for arg in grandChild:
                                argument = Argument(arg.text, arg.attrib.get("type"),  
                                arg.attrib.get("descr"), arg.attrib.get("min"), 
                                arg.attrib.get("max"), arg.attrib.get("unit"))

                                command.fillResponse(argument)

                    commands.append(command)

    print(commands)
    for i in range(len(commands)):
        # print(commands[i].name ,commands[i].prepareRequest(), commands[i].request[0])
        if commands[i].name == 'set_humidity_gradient_up':
            commands[i].setValue(29.23)

    for i in range(len(commands)):
        print(commands[i].name ,commands[i].prepareRequest(), commands[i].request[0])


if __name__ == "__main__":
    xmlParser = XmlProtocolParser()
    # sshSender = SshProtocolSender()

    # commands = xmlParser.getCommands()
    # commands["read_temperature"]
    # print(sshSender.execCommand("pwd; mkdir t123; ls; ls"))
    # if sshSender.checkConnection():
        # print(sshSender.execCommand("python3 .py arg"))


    importCommandsFromXml()