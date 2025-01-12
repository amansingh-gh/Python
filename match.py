#If you learn c aur c++ then we use switch statement here we use the same as named are match case statement.

print(":::::::::::::::Please Enter Your Value Between 1 to 5:::::::::::::::")
x = int(input("Enter the value of x: "))

match x:
    case 1:
        print("The value and the case is 1")
    case 2:
        print("The value and the case  is 2")
    case 3:
        print("The value and the case is 3")
    case 4:
        print("The value and the case is 4")
    case 5:
        print("The value and the case is 5")
    
# For adding default as C we use case _
    case _:
     print("Invalid Entry")
