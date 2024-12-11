print("SINH VIEN : DINH XUAN ANH")
print("MSV : 235752021610055")
class IOString:
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Nhập vào một chuỗi: ")

    def print_String(self):
        print(self.str1.upper())
str1 = IOString()
str1.get_String()
str1.print_String()
