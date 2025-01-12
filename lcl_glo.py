x = 40
y = 100
def my_fun():
    global y
    global x
    x = 50
    # y = 90
    # print("This is the value of x :",x)
my_fun()
print(y)
print(x)