#create a varibal outside a function
x = "awesome"
def myfunc():
    print("Pythos is " +x)
myfunc()

#create a varibal inside a function
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " +x)

myfunc()
print("Python is " +x)

#global keyword

def myfunc():
    global x
    x = "fanastic"

myfunc()
print("Python is " +x)