def msge(fx):
    def greet():
        print("HEllo everyone")
        fx()
        print("Thank You")
    return greet()

@msge
def aman():
    print("This is decorator")