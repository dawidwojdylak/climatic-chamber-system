# xml interface protocol parser
import xml.etree.ElementTree as ET
from Command import *
from Argument import *
from Communicator import Communicator

class XmlProtocolParser:
    """Class containing parser for XML commands' protocol"""
    def __init__(self, filePath="./CTS_Interface_Protocol.xml"):
        """The constructor takes path to the XML Commands file as an argument"""
        self.filePath = filePath
        self.commands = []
        self.tree = None
        self.root = None
        try:
            self.tree = ET.parse(self.filePath)
            self.root = self.tree.getroot()
            # if root.tag == "commands":
                # for child in root:
                    # self.commandsDict.update({child.attrib.get("name") : child.find("request").text})
        except Exception as e:
            Communicator.eprint("Exception: " + str(e))

    def importCommandsFromXml(self):
        """This metod parser XML into Commands (containing Arguments)"""
        root = self.root

        if root.tag == "commands":
            for child in root:
                command = Command(child.attrib.get("name"))
                command.setCommandType(child.attrib.get("type"))
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

                self.commands.append(command)
            return self.commands

    def getCommands(self):
        return self.commands
    def getRoot(self):
        return self.root

    def getCommand(self, commandName: str):
        """Returns the particular command"""
        for com in self.commands:
            if com.name == commandName:
                return com
        return None



if __name__ == "__main__":
    parser = XmlProtocolParser()
    rt = parser.getRoot()
    for cd in rt:
        print(cd.attrib, cd.tag, cd.text)