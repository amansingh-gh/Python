class person_details:
    def __init__(self, name, grade):
        self.nam = name
        self.gde = grade

    def info(self):
        print(f'My name is {self.nam} and grade is {self.gde}')

emp1=person_details('Mohan', '4')
emp2=person_details('Soname', '4')
emp3=person_details(1,2)

emp1.info()
# print(f"My name is {emp1.nam} and my grade is {emp1.gde}")
# print(f"My name is {emp2.nam} and my grade is {emp2.gde}")
# print(f"My name is {emp3.nam} and my grade is {emp3.gde}")
