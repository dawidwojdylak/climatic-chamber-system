class ResponseSimulator():
    def sendCommand(self, cmd : str):
        s = cmd[0]
        if s == 'T':
            return 'T101112082715'
        elif s == 't':
            return cmd
        elif s == 'A':
            return cmd + " 020.4 023.0"
        elif cmd == 'Aa':
            return "A00_020.4_023.0/01_080.7_014.8/02_020.4_023.0"
        elif s == 'a':
            return 'a'
        elif s == 'u':
            return 'u'
        elif s == 'd':
            return 'd'
        elif cmd.startswith('U0'):
            return 'U0 005.0 003.0'
        elif cmd.startswith('U1'):
            return 'U1 005.0 003.0'