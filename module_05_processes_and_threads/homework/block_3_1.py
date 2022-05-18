import sys


class MyManager:
    def __init__(self, new_stdout, new_stderr):
        self.stdout = new_stdout
        self.stderr = new_stderr

    def __enter__(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stdout.close()
        self.stderr.close()


if __name__ == '__main__':
    with MyManager(
            new_stdout=open('stdout.txt', 'a', encoding='utf-8'),
            new_stderr=open('stderr.txt', 'a', encoding='utf-8')
    ):
        print('ТЕКСТ stdout')
        print(12/0)
        raise ZeroDivisionError
