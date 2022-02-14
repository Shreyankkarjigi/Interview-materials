#Method overloading in python

#Method overloading in Python is a feature that allows the same operator to have different meanings

#Overloading is the ability of a function or an operator to behave in different ways based on the parameters that are passed to the function, or the operands that the operator acts on.

#Create a class called person

class Person:

    def Hello(self,name=None):
        #if name is blank
        if name is not None:
            print("hello"+name)

        else:
            print("Heloo")

#create instance

person1=Person()

#call the method

person1.Hello()

#call same function with parameter

person1.Hello("shreyank")


