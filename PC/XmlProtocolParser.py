# xml interface protocol parser
import xml.etree.ElementTree as ET

class XmlProtocolParser:
    def __init__(self, filePath="C:\\Users\\446UXR\\Projects\\Praca_dyplomowa\\PC\\CTS_Interface_Protocol.xml"):
        self.filePath = filePath
        self.commandsDict = {}
        self.tree = None
        try:
            self.tree = ET.parse(self.filePath)
            root = self.tree.getroot()
            if root.tag == "commands":
                print(root)
                for child in root:
                    self.commandsDict.update({child.attrib.get("name") : child.find("value").text})
                print(self.commandsDict)
        except Exception as e:
            print("Exception: ", end='')
            print(e)

    def getCommands(self):
        return self.commandsDict



if __name__ == "__main__":
    parser = XmlProtocolParser()
