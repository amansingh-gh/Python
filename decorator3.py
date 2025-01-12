def pink(func1):
    def green():
        print("This is the upper part")
        func1()
        print("This is the next line of upper part")
    return green

@pink
def blue():
    print("This is the decorator line")
blue()