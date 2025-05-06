class Animal:
    def sound(self):
        print("Animal makes sound")

class Cat(Animal):
    def noise(self):
        print("Cat say meow")

d = Cat()
d.sound()
d.noise()