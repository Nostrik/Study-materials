class MyManager:
    def __init__(self, path: str, mode, ex_list):
        self.name = path
        self.mode = mode
        self.exceptions = ex_list

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            print('Exception was skipped')
            return True
        print("Exception {} has been handled".format(exc_type))
        self.file.close()


if __name__ == '__main__':
    ignore_exceptions = (ValueError, AttributeError)
    with MyManager('test_input.txt', 'r', ignore_exceptions) as file:
        s = file.read()
        print(s)
        raise ValueError
