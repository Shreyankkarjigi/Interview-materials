#Inheritance in classes

#inheritance is used when we want to have functions from one class in another class too

#Lets create a class called A

class A:

    #create a function1 in class A

    def function1(self):
        print("Function1")


#similiary create class B

class B:

    #create a function2 in class B

    def function2(self):
        print("Function2")

#similiary create class C

class C:

    #create a function3 in class C

    def function3(self):
        print("Function3")



#Now suppose class C wants functions present in both Class A and class B

#we can do that in following way


#inside class C we can reference the classes from which we need the functions

class C(A):

    #create a function3 in class C

    def function3(self):
        print("Function3")

#so now in class C we passed refrence of class A 


#so now when we call class C instance we get functions of class A too

c1=C()

print(c1.function1)
print(c1.function3)

#similiary we can have mutiple classes 

class C(A,B):

    #create a function3 in class C

    def function3(self):
        print("Function3")

#Now class C will have functions of both class A and B