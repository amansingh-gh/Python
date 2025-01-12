class Car:
    wheels=5

    def __init__(self):
        self.company = "BMW"
        # self.wheels = 4

c1=Car()
Car.wheels = 10
print(c1.company, c1.wheels)
print(c1.wheels)
