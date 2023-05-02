# ppy/manage_file.py


class MangeFile:
    def __init__(self):
        None

    def create_file_hello(self):
        with open("hello.py", "w") as f:
            f.write('print("Hello, World")')

    def create_file_py(self, file_dot_py):
        with open(f"{file_dot_py}", "w") as f:
            f.write("")
