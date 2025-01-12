try: 
    x = int(input("Enter the number: "))
    if(x<50):
        print("Your number is smaller then 50")
    elif(x==50):
        print("Your number is equal to 50")
    else:
        print("Your number is greater then 50")
except:
    print("Invalid Input")
finally:
    print("-------This is end of the program---------")