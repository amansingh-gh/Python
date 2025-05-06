import smtplib

sender_mail = "xyz@gmail.com"
password = "Password"
receiver_mail = "abc@gmail.com"

#for multiple users bound under -> [ "abc@gmail.com", xyz@gmail.com, "kyp@gmail.com"] 

message = "This is me !!"

server = smtplib.SMTP("smtp@gmail.com",587)
server.login(sender_mail, password)
server.sendmail(sender_mail,receiver_mail,message)
server.quit()

print("Message Sent Successfully")