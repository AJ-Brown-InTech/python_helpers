# send emails from python
import smtplib
my_email = input("Enter your email: ")#you can hardcode but like security
passw =  input("Enter your password: ")#you can hardcode but like security
# great resource to understand port diffrences(https://www.mailgun.com/blog/email/which-smtp-port-understanding-ports-25-465-587/#subchapter-5)
connection = smtplib.SMTP("smtp.gmail.com", 587) 
#protocol for emails = tls
connection.starttls()
connection.login(user = my_email, password=passw)

connection.sendmail(from_addr=my_email)
to_email = input("Enter the email you want to send a message to: ")
body = input("Enter your message: ")
to_addrs = to_email, msg = body
connection.close()

#not working link(https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp)