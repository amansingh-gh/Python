a = int(input("Enter the number between 5 and 9: \n"))
if (a<5 or a>=9):
    raise ValueError("You should be 5 and 9")