def summ(arm):
    def pink():
        print("This is pink colour")
        arm()
        print("This is the after pink line")
    return pink

@summ
def nowcheck():
    print("Now this is the decorator part")
nowcheck()