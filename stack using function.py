#stack using function
'''
stack are linear data structure that uses a one way list to enter and remove elements

in stack elements are entered and removed from same side, it is based on LIFO (last in,first out) approach
i.e. element added last to stack will be removed first

push() is used to add elements to list
pop() is used to remove elements from list
'''
#define a list of elements
stack=[]
#def push function,with a list as parameter
def push(stack):

    for i in range(5):

        print("adding element",i,"to list")
        stack.append(i)


    print(stack)

#def pop function

def pop(stack):

    for j in range(5):

        print("Removing element",stack.pop(),"from list")


    print(stack)

    #check if stack is empty

    if not stack:
        print("stack is empty")



print(push(stack))
print(pop(stack))

'''
output

adding element 0 to list
adding element 1 to list    
adding element 2 to list    
adding element 3 to list    
adding element 4 to list    
[0, 1, 2, 3, 4]
None
Removing element 4 from list
Removing element 3 from list
Removing element 2 from list
Removing element 1 from list
Removing element 0 from list
[]
stack is empty

'''




