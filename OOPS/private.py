class student:
    def __init__(self):
        self.nomangled = "This is no mangled"
        self.mangled = "This is mangled"
stu1=student()
# print(stu1.__mangled)
print(stu1._student__nomangled)