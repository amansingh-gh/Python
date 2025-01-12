# basic
print("Hello")

# comment

# varibale
a = 3
b = 5.5
print(a + b)

# string
d = "Tom"
print(d)

# Arithmetic Operator ( +, - , *, /, //, % )
x = 10
y = 2
print(int(x % y))  # remainder

# comparison operator  >, <, !>, !<, ==, !=
# Logical Operator
# Bitwise operator


# loops:
# for loop
num = int(input("Enter a number: "))
for i in range(num):
    print(i + 1)

# while loop
print("This is while loop: \n")
x = int(input("Enter a value: "))
while x < 20:
    print(x * x)
    x + 1


# function
def honk(name):
    return f"{name} is honking"

message = honk("Bike")
print(message[0:3])


# List
l1 = [3, 5, 7, 8, "Harry"]
print(l1)
l1.extend([23, 24, 25, 23])
print("Iteration is: ")
for i in l1:
    print(i, " ")


# set
l2 = (3, 5, 7, 8, "Harry")
for i in l2:
    print(i, " ")


# // Dictionary
Dict = {"Hello": "World", "Sam": "sabun", "Good": "To see You"}
print(Dict)
for i in Dict:
    print(f"{i} : {Dict[i]}")


# if-else-elif
age = int(input("Enter your age: "))
if (age >= 18):
    print(f"You can drive because your age is {age}")
elif (age < 0 & age > 100):
    print("Invalid Input")
else:
    print("You cannot vote")



# exception handling
try:
    num = int(input("Enter a number: "))
    print(num + 10)
except Exception as e:
    print("Something went wrong ",e)
finally:
    print("have a great day")

#
# FILE IO
# Writing a file
s = "harry is a good person"
with open("../fileIO/test.txt", "w") as f:
    f.write(s);

# appending a file
with open("../fileIO/test.txt", "a") as fa:
    fa.write("This is also good\n")
#Reading a File
fp = open("../fileIO/test.txt", "r")
s = fp.read()
print(s)
fp.close()