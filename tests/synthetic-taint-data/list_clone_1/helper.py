import subprocess

def run_cmd(cmd: str, msg: str="Failed to run command") -> None:
    print('Running ' + ' '.join(cmd))
    print(cmd)
    if subprocess.check_call(cmd):
        print(msg)
        exit(1)