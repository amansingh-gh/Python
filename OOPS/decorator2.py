def msge(fx):
    def mfx():
        print("HElloo Good morning")
        fx()
        print("Thanks for choosing me")
    return mfx()

@msge
def aman():
    print("Let us check this will work or not")