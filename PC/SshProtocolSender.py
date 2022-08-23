import paramiko


class SshProtocolSender:
    def __init__(self, ip_addr = '10.224.157.83', usnm = 'test', psswd = 'test') -> None:
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # niebezpieczne, weryfikowac manualnie
        self.ssh.connect(ip_addr, username=usnm, password=psswd)

    def execCommand(self, command):
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(command);
        return ssh_stdout.readlines()

    def checkConnection(self):
        return self.ssh.get_transport().is_active()
