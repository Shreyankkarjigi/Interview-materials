#method overriding in classes

#create a parent class with a value as 4

class Parent:
    def __init__(self):
        self.value=4
#create another class that returns the value we set earlier
    def get_value(self):
        return self.value



#now we will create a child class that inherits from parent class

class Child(Parent):

    #create same method called get_value and update the self value by adding +1

    def get_value(self):
        return self.value+1


#create instance of Child class

c=Child()
#call the get value function on child 
print(c.get_value())


#ouput:5

#This is called as method overriding , we overrid the get_value() method defined in our parent class in child class.