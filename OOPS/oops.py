class person:
    def info(self):
        print(f"My name is {self.name} and my occpation is {self.occupation}")

a=person()
b=person()

a.name = "Ankit"
b.name = "Sonam"

a.occupation = "HR"
b.occupation = "Clerk"

b.info()