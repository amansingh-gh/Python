num = int(input("Enter checking number: "))
match num:
    case 1:
        print("Lets drink Coffee")
    case 2:
        print("Lets drink Tea")

    case _ if num!=90:
        print("Entry 90 not matched")
    case _ if num!=80:
        print("Entry 80 not matched")
