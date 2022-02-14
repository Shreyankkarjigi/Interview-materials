#classes with constructors

# A constructors/Initiliazors are used to create a template for objects in a class

# This comes in handy when there are many instances and all have same properties


#define a person class

class Person:

    #define a init method with all the required parameters

    def __init__(self,name,age):

        #self is used to refer same class

        self.name=name
        self.age=age
      


#create instances of class and pass the argument to the parameters

person1=Person('shreyank',22)
person2=Person('viraj',21)

print(person1.name)
print(person2.age)



