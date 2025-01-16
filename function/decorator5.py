def parrot(func1):
    def hen():
        print('This is the upper line')
        func1()
        print('This is the second line')
    return hen

@parrot
def piro():
    print('This is the decorator line')
piro()