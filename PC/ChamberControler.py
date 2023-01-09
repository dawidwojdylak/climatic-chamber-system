import XmlProtocolParser as xml
import SshProtocolSender as ssh

class ChamberControler:
    def updateCommandList(self):
        """Updates command list and ip"""
        self.commandList = self.xmlParser.getCommands()
        self.ip = self.xmlParser.getIp()
        return self.commandList

    def getCommands(self):
        return self.commandList

    def importXmlFile(self, filename):
        """Imports """
        self.xmlParser = xml.XmlProtocolParser(filename)
        self.xmlParser.importCommandsFromXml()
        self.commandList = self.xmlParser.getCommands()
        self.ip = self.xmlParser.getIp()
        if self.ip != None:
            self.sshSender = ssh.SshProtocolSender(self.ip)
        else:
            self.sshSender = ssh.SshProtocolSender()
        self.currentCommand = None
        return self.commandList

    def sendCommandToChamber(self, cmd):
        request = cmd.prepareRequest()
        try:
            response = self.sshSender.execCommand(request)
        except Exception:
            raise
        result = cmd.parseChamberResponse(response)
        return result

    def getCommand(self, commandName : str):
        for c in self.commandList:
            if c.getName() == commandName:
                return c
        return None

