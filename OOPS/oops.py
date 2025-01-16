class Employee:
    def __init__(self, fname, lname, sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal
emp1 = Employee('Aman', 'Singh', 500000)
emp2 = Employee('Tony', 'Stark', 400000)

print(emp2.sal)
print(emp2.lname)