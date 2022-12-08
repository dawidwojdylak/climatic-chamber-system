import XmlProtocolParser as xml
import SshProtocolSender as ssh
import ChamberResponseSimulator as simulator

class ChamberControler:
    def __init__(self, xmlConfigPath):
        self.xmlParser = xml.XmlProtocolParser(xmlConfigPath)
        self.xmlParser.importCommandsFromXml()
        self.commandList = self.xmlParser.getCommands()
        # self.sshSender = ssh.SshProtocolSender()
        self.respSimulator = simulator.ResponseSimulator()

        self.currentCommand = None

    def parseXml(self, xmlFilePath):
        self.xmlParser = xml.XmlProtocolParser(xmlFilePath)

    def updateCommandList(self):
        self.commandList = self.xmlParser.getCommands()

    def getCommandsNamesList(self):
        return [i.getName() for i in self.commandList]
    
    def getCommands(self):
        return self.commandList

    def sendCommandToChamber(self, commandName : str):
        pass        
    
    def sendCommandToChamber(self, cmd):
        request = cmd.prepareRequest()
        response = self.respSimulator.sendCommand(request)
        # TODO: prepare (parse) response
        return cmd.parseChamberResponse(response)


if __name__ == "__main__":
    cc = ChamberControler("./CtsInterfaceProtocol.xml")
    print("...ChamberControler...")
    testCommmandList = cc.getCommandsNamesList()

