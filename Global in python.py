#Global variables
'''
he basic rules for global keyword in Python are:

   1. When we create a variable inside a function, it is local by default.

   2.When we define a variable outside of a function, it is global by default. You don't have to use global keyword.

   3. We use global keyword to read and write a global variable inside a function.

    
   4.Use of global keyword outside a function has no effect.
'''

#example 1 

#Accessing global variable from inside a function

c=1 #variable outside the function is global by default

def add():
    print(c)

#call the function

add()


#example 2

#Modifying Global Variable From Inside the Function
'''
d=1

def add1():
    d=d+2 #increment value of d by 2

    print(d)

#call function

add1()

#when we run this we get following error

# UnboundLocalError: local variable 'd' referenced before assignment
'''

#To fix this error we will make the "e" variable global

e=1

def add2():
    #make 'd' as global
    global e
    e=e+2 #increment value of d by 2

    print(e)

#call function

add2()


#now we get ouput as 3