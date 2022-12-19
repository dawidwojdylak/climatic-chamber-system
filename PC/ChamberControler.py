import XmlProtocolParser as xml
import SshProtocolSender as ssh
import ChamberResponseSimulator as simulator

class ChamberControler:
    def __init__(self, xmlConfigPath):
        self.xmlParser = xml.XmlProtocolParser(xmlConfigPath)
        self.xmlParser.importCommandsFromXml()
        self.commandList = self.xmlParser.getCommands()
        self.ip = self.xmlParser.getIp()
        if self.ip != None:
            self.sshSender = ssh.SshProtocolSender(self.ip)
        else:
            self.sshSender = ssh.SshProtocolSender()
            # raise AssertionError("Unexpected value of 'self.ip'!: ", self.ip)
        # self.respSimulator = simulator.ResponseSimulator()
        self.currentCommand = None


    def updateCommandList(self):
        self.commandList = self.xmlParser.getCommands()
        self.ip = self.xmlParser.getIp()
        return self.commandList

    def getCommands(self):
        return self.commandList

    def importXmlFile(self, filename):
        self.xmlParser.importXmlFile(filename)
        self.xmlParser.importCommandsFromXml()
        self.commandList = self.xmlParser.getCommands()
        return self.commandList

    def sendCommandToChamber(self, cmd):
        request = cmd.prepareRequest()
        try:
            response = self.sshSender.execCommand(request)
        except Exception:
            raise
        result = cmd.parseChamberResponse(response)
        return result



