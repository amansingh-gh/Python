def fun():
    try:
        l = [12,18,21,25,27,88]
        i=int(input("Enter Your index: "))
        print(l[i])
        return 1
    except:
        print("some error occurs")
        return 0
    finally:
        print("This is always executed")

x=fun()
# print(x)