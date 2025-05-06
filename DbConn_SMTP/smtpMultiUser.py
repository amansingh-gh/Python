import smtplib
with open("user.txt", "r") as file:
    user = file.readlines()

sender = "abc@gmail.com"
password = "PASSWORD"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender,password)

for i in user:
    name,email = i.strip().split(",")
    message = "Hey I'm Good"
    server.sendmail(sender,email,message)
    print("Mail Sent Successfully")

server.quit()