class MyManager:
    def __init__(self, path: str, mode, ex_list):
        self.name = path
        self.mode = mode
        self.exeptions = ex_list
        # print(self.exeptions)

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exception {} has been handled".format(exc_type))
        self.file.close()
        return True


if __name__ == '__main__':
    ignore_exceptions = FileNotFoundError
    with MyManager('test_input.txt', 'r', ignore_exceptions) as file:
        s = file.read()
        print(s)
