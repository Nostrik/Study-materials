import subprocess
import shlex


def run_program():
    res = subprocess.run(['python', 'test_program.py'], input=b'some input\notherinput')
    print(res)
    # print("stdout", res.stdout)
    # print("stderr", res.stderr)
    # command_str = 'ps'
    # token = shlex.quote(command_str)
    # res = subprocess.run(token, shell=True)
    # print(res.stdout)


if __name__ == '__main__':
    run_program()
