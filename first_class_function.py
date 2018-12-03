#first-class function in Python


def name():
    print('My Name is Rajesh Pudasaini')

my_fun = name #assigning function as a variable

def your_name(nam):
    nam()

your_name(my_fun) #assigned function as a arguments

intro = input('What is your Name ?')

def outside():
    def inside(name):
        print(name.upper())
    
    return inside(f'Hello! {intro}')#returning the function from one funtion


outside()




