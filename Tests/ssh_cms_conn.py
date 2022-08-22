import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # niebezpieczne, weryfikowac manualnie
ssh.connect('10.224.157.83', username='test', password='test')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("uptime")
print(ssh_stdout.readlines())