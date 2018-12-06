import os
#opens file to write data on it
#f = open("hello.txt","w")
#f.write("Hi You are created")
#f.close()#close the opened file

#open the file to read 
f = open("hello.txt","r")
que = f.read()
f.close()

ques = "@razyesh_pudasaini"
print(ques)
print(que)

if (que == ques):
    f = open("ans.txt")
    print(f.read())
else:
    print("No User Found")

if os.path.exists("hi.txt"):
    os.remove("hi.txt")
else:
    print("File Doesnot exist")