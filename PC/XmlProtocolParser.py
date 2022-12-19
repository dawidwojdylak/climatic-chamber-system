# xml interface protocol parser
import xml.etree.ElementTree as ET
from Command import *
from Argument import *

class XmlProtocolParser:
    """Class containing parser for XML commands' protocol"""
    def __init__(self, filePath="./CtsInterfaceProtocol.xml"):
        """The constructor takes path to the XML Commands file as an argument"""
        self.filePath = filePath
        self.commands = []
        self.tree = None
        self.root = None
        self.importXmlFile(filePath)

    def importXmlFile(self, filePath):
        """Imports XML file"""
        self.commands.clear()
        self.filePath = filePath
        try:
            self.tree = ET.parse(self.filePath)
            self.root = self.tree.getroot()
        except Exception:
            raise

    def importCommandsFromXml(self):
        """This metod parser XML into Commands (containing Arguments)"""
        root = self.root
        self.ip = None
        self.chamberName = 'Default name'
        if root.tag == "commands":
            for child in root:
                if child.tag == "command":
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
                if child.tag == "config":
                    for grandChild in child:
                        if grandChild.tag == "ip":
                            self.ip = grandChild.text
                        elif grandChild.tag == "chamberName":
                            self.chamberName = grandChild.text
            return self.commands

    def getCommands(self):
        return self.commands
    def getRoot(self):
        return self.root
    def getIp(self):
        return self.ip
    def getChamberName(self):
        return self.chamberName

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