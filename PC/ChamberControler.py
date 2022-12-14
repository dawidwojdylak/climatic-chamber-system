import XmlProtocolParser as xml
import SshProtocolSender as ssh
import ChamberResponseSimulator as simulator

class ChamberControler:
    def __init__(self, xmlConfigPath):
        self.xmlParser = xml.XmlProtocolParser(xmlConfigPath)
        self.xmlParser.importCommandsFromXml()
        self.commandList = self.xmlParser.getCommands()
        self.sshSender = ssh.SshProtocolSender()
        # self.respSimulator = simulator.ResponseSimulator()
        self.currentCommand = None

    def updateCommandList(self):
        self.commandList = self.xmlParser.getCommands()
        return self.commandList

    def getCommands(self):
        return self.commandList

    def sendCommandToChamber(self, cmd):
        request = cmd.prepareRequest()
        # response = self.respSimulator.sendCommand(request)
        response = self.sshSender.execCommand(request)
        return cmd.parseChamberResponse(response)



