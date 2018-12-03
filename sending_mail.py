import smtplib
#creates SMTP Session
s = smtplib.SMTP('smtp.gmail.com', 587)

#start TLS for security
s.starttls()

#authentication
s.login("pudasainirajesh504@gmail.com","your_password")

#number of email to sent the mail
email = input('Enter Your Email:')

#message to be sent
message = "Hi I am sending the message by using Python code"

#sending the mail
s.sendmail('pudasainirajesh504@gmail.com',email,message)

#terminating the session
s.quit()

