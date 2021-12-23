import smtplib
from email.message import EmailMessage


msg = EmailMessage()

msg['Subject'] = "Sending Email Test"
msg['From']    = "Moin Malik"
msg['To']      = "moin.malik996@gmail.com"
msg.set_content("This is my Content")


print("Sending Email\n\n")
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("your_email", "your_password")
server.send_message(msg)
print("Email_Sent")
server.quit()




