import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",        # or your server IP
    user="your_username",
    password="your_password",
    database="your_database" # optional if just connecting
)

# Create a cursor object
cursor = conn.cursor()

# Example: Show databases
cursor.execute("SHOW DATABASES")

# Print the databases
for db in cursor:
    print(db)

# Close connection
cursor.close()
conn.close()
