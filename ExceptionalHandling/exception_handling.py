try:
    num = int(input("Enter numbers only: "))
    # print(num)
    a=[3,7]
    print(a[num])
        
# except ValueError:
#     print("Your entry is not integer")
    
except IndexError:
    print("index not found")