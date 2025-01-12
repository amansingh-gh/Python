def pink(func1):
    def green():
        print("This is the upper line")
        func1()
        print("This is the next line")
    return green

@pink
def red():
    print("This is the decorator line")
red()