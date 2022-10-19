# xml interface protocol parser
import xml.etree.ElementTree as ET
from Command import *
from Argument import *

class XmlProtocolParser:
    def __init__(self, filePath="C:\\Users\\446UXR\\Projects\\Praca_dyplomowa\\PC\\CTS_Interface_Protocol.xml"):
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
            print("Exception: ", end='')
            print(e)

    def importCommandsFromXml(self):
        root = self.root

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

                self.commands.append(command)
            return self.commands

    def getCommands(self):
        return self.commands
    def getRoot(self):
        return self.root



if __name__ == "__main__":
    parser = XmlProtocolParser()
    rt = parser.getRoot()
    for cd in rt:
        print(cd.attrib, cd.tag, cd.text)