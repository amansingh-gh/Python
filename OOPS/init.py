class company:
    def __init__(self, nam, occ):
        self.name = nam
        self.occupation = occ

        def info(self):
         print(f"My name is {self.nam} and my posititon in company is[{self.occ}")

a=company('rohan','manager')
print(f"My name is {a.name} and my occupation is {a.occupation}")