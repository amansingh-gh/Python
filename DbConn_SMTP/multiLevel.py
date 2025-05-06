class GrandPrent:
    def intro1(self):
        print("Grandparent")


class Parent(GrandPrent):
    def intro2(self):
        print("Parent")

class Child(Parent):
    def intro3(self):
        print("Child")

d = Child()
d.intro1()
d.intro2()
d.intro3()