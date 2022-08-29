# xml interface protocol parser
import xml.etree.ElementTree as ET

class XmlProtocolParser:
    def __init__(self, filePath="C:\\Users\\446UXR\\Projects\\Praca_dyplomowa\\PC\\CTS_Interface_Protocol.xml"):
        self.filePath = filePath
        # self.commandsDict = {}
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

    

    # def getCommands(self):
        # return self.commandsDict
    def getRoot(self):
        return self.root



if __name__ == "__main__":
    parser = XmlProtocolParser()
    rt = parser.getRoot()
    for cd in rt:
        print(cd.attrib, cd.tag, cd.text)