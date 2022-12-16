import paramiko


class SshProtocolSender:
    def __init__(self, ipAddr = '10.224.157.83', usnm = 'test') -> None:
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 
        self.username = usnm
        self.ipAddress = ipAddr

    def __del__(self):
        self.logOut()

    def execCommand(self, command):
        try:
            cmd = "python3 ~/chamber.py \"" + command + "\""
            ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(cmd, timeout=10)
            return ssh_stdout.readlines()
        except Exception:
            print(Exception)
            return "Response error"

    def checkConnection(self) -> bool:
        try:
            return self.ssh.get_transport().is_active()
        except Exception as e:
            print(e)
            return False

    def setUsername(self, username):
        self.username = username

    def setIp(self, ip):
        self.ipAddress = ip
    
    def logIn(self, passwd, username = None, ipAddr = None):
        if username: self.username = username
        if ipAddr:   self.ipAddress = ipAddr
        print(self.ipAddress, self.username, passwd)
        try:
            self.ssh.connect(self.ipAddress, username=self.username, password=passwd, auth_timeout=10., timeout=10.)
        except Exception as e:
            print(e)

    def logOut(self): # important
        self.ssh.close()
