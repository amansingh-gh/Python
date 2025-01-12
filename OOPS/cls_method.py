class Student:
    leaves=8
    def __init__(self, name, roll):
        self.name=name
        self.roll=roll

    @classmethod
    def change_leaves(cls, newleaves):
        cls.leaves=newleaves

stud1=Student("Rahul", 50)
stud2=Student("Hotly", 40)

Student.change_leaves(999)

print(stud1.name , stud1.roll)
print(stud2.name , stud2.roll)

print(stud1.leaves)
print(stud2.leaves)