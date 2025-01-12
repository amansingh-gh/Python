def decorator(func1):
    def execute():
        print("Executing now")
        func1()
        print("Executed")
    return execute

@decorator
def hiii():
    print("This is decorator part")
hiii()