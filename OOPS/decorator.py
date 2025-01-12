def dec (fun1):
    def pink():
        print("This is the first/upper line")
        fun1()
        print("This the the last line")
    return pink
@dec
def new():
    print("This is the decorator line")
new()