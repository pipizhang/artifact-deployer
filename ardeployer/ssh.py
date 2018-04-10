import shlex
import paramiko

class SSHClient:
    def __init__(self) -> None:
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()

    def connect(self, server: str, username: str, port: int=22) -> None:
        self.client.connect(server, username=username, port=port)

    def exec_command(self, command: str) -> str:
        stdin, stdout, stderr = self.client.exec_command(command)
        out = stdout.read()
        return out.decode("utf-8")

    def upload(self, local_file: str, remote_file: str) -> bool:
        sftp = self.client.open_sftp()
        sftp.put(local_file, remote_file)
        sftp.close()
        check = self.exec_command('ls {}| wc -l'.format(shlex.quote(remote_file)))
        return int(check) == 1

    def close(self) -> None:
        self.client.close()
