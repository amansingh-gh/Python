import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="rosdt",
  password="1234",
  database="mysql"
)

if(mydb):
    print("connected to mysql server")
else:   
    print("failed to connect with mysql server")
    exit(1)
    
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS custumber (name VARCHAR(255), address VARCHAR(255))")
print("table created")
mycursor.execute("insert into custumber values('Akshat','Bihar')")
mycursor.execute("insert into custumber values('Anshu','delhi')")
mydb.commit()

mycursor.execute("select * from custumber")

custumber_list=list()
custumber_list=mycursor.fetchall()

for e in custumber_list:
    print(e)