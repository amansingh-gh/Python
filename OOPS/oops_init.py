class Employee:
    no_of_leafes = 40
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
@classmethod
def change_leafes(cls, newleafes):
    cls.no_of_leafes = newleafes

jonny = Employee("Jon", 50, "pppppp")

jonny.change_leafes(888)
print(jonny.age ,jonny.location, jonny.name)
print(jonny.no_of_leafes)