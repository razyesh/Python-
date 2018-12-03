import fbchat
from getpass import getpass
username = str(input("Username: "))
client = fbchat.Client(username, getpass())

name = str(input("Name: "))
friends = client.searchForUsers(name)
msg = str(input("Message: "))
sent = client.send(friends, msg)
if sent:
    print("Message Sent Successfully")

