class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        print(f"The name is {self.name} and id is {self.id}")
emp = employee("Rohan" , 50)
emp.details()
