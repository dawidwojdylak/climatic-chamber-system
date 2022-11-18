class ResponseSimulator():
    def sendCommand(self, cmd : str):
        s = cmd[0]
        if s == 'T':
            return 'T101112082715'
        elif s == 't':
            return cmd
        elif s == 'A':
            return cmd + " 020.4 023.0"