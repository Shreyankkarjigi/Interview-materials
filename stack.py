#stacks in python

#stack using lists


#stacks work on LIFO approach that is Last in , first out 

#so whats insterted last comes out first

#in lists pop() is used to remove last element from the list


stack=[]

n=int(input("enter total elements in stack\n"))

for i in range(n):

    e=int(input("input element"))

    #append to stack


    stack.append(e)

    print(stack)


#pop elements now
print("removing elements from stack")
for j in range(n):

    stack.pop()
    print(stack)


#if stack is empty print empty

if not stack:
    print("stack is now empty")


else:
    print("stack is not empty")

'''
output

enter total elements in stack
5
input element1
[1]
input element2
[1, 2]       
input element3
[1, 2, 3]    
input element4
[1, 2, 3, 4] 
input element5
[1, 2, 3, 4, 5]
removing elements from stack
[1, 2, 3, 4]
[1, 2, 3]
[1, 2]
[1]
[]
stack is now empty







'''