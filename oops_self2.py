class Employee:
    def showdetails(self):
        print(f"The full name of sohan is {sohan.name}\nHer age is {sohan.age}\nHe lived in {sohan.location}")
        # print(f"The full name of sohan is {Ronny.name}\nHer age is {Ronny.age}\nHe lived in {Ronny.location}")
        
sohan = Employee()
Ronny = Employee()

sohan.name = "Sohan Sarabi"
sohan.age  = 200
sohan.location = "Sarab Ki Nagri"

Ronny.name = "Ronny Thakur"
Ronny.age = 44
Ronny.location = "Nibba Palace"

print(sohan.showdetails())
# print(Ronny.showdetails())