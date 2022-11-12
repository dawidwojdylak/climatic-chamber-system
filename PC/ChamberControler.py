import XmlProtocolParser as xml
import SshProtocolSender as ssh

class ChamberControler:
    def __init__(self, xmlConfigPath):
        self.xmlParser = xml.XmlProtocolParser(xmlConfigPath)
        self.xmlParser.importCommandsFromXml()
        self.commandList = self.xmlParser.getCommands()
        # self.sshSender = ssh.SshProtocolSender()

    def parseXml(self, xmlFilePath):
        self.xmlParser = xml.XmlProtocolParser(xmlFilePath)

    def updateCommandList(self):
        self.commandList = self.xmlParser.getCommands()

    def getCommandsNamesList(self):
        return [i.getName() for i in self.commandList]

    


if __name__ == "__main__":
    cc = ChamberControler("/home/dawidwojdylak/Projects/mip_pr-climatic_chamber_system/PC/CTS_Interface_Protocol.xml")
    print("...ChamberControler...")
    testCommmandList = cc.getCommandsNamesList()

