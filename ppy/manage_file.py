# ppy/manage_file.py


class MangeFile:
    def __init__(self):
        None

    def create_file_hello(self):
        with open("hello.py", "w") as f:
            f.write('print("Hello, World")')

    def create_file_convert_money(self):
        with open("convert_money.py", "w", encoding="utf-8") as f:
            f.write(
                """
def main():
    dollar = bath_to_dollar(input("Enter bath: "))
    yen = dollar_to_yen(dollar)
    print("You have", dollar, "dollars and", yen, "yen")
    

def bath_to_dollar(d):
    # แก้โค้ด

def dollar_to_yen(p):
    # แก้โค้ด

main()
"""
            )

    def create_file_py(self, file_dot_py):
        with open(f"{file_dot_py}", "w") as f:
            f.write("")
