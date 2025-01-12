class Truck:
    wheels = 8
    def __init__(self):
        self.company = "Tata"

t1 = Truck()
Truck.wheels=10
print(t1.company)
print(t1.wheels)
