class Student:
    salary = 89

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary


rohan = Student("Rohan", "49999")
print(rohan.salary)
print(rohan.name)
