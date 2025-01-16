class Student:
    def printdetails(self):
        return f"The name of stud1 {self.name}"

stud1 = Student()
stud2 = Student()
stud3 = Student()

stud1.name = "Soon"
stud2.name = "Poon"
stud3.name = "Roon"

print(stud1.printdetails())