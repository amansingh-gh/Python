class Calculator:
    def add(self, a, b=0, c=0):  # Simulating overloading
        return a + b + c
    def add(self, a):  # Simulating overloading
        return a + b + c
    def add(self, a=0, b=0, c=10):  # Simulating overloading
        return a + b + c

calc = Calculator()
print(calc.add(5))         # 5
print(calc.add(5, 3))      # 8
print(calc.add(5, 3, 2))   # 10
