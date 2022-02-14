#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
'''
Take a list L from user, add 5 numbers to it.
After adding 5 numbers to the list ask user for index value ;i' and a new element e
Add the new element at given index.
Note:Max elements are 5 only.
'''
l=[]
ind=[]

for i in range(1,5):

    x=int(input('Enter element\n'))
    l.append(x)
print("Your entered elements are:\n")
print(l)

y=input("do you want to update the list,Y or N\n")


if y=="Y":
    for i in range(1,5):
        ind.append(l.index(i))
    print(ind)
        
        #lets make it neat, lets provide user with a dictionary that has Index:Value

    print("Following shows Index:Value")
    print(dict(zip(ind,l)))

    i=int(input("Input index value where you want to update the element"))

    if i>5:
        print("Invalid index , Please enter index value in given range")
    else:

        e=int(input("Enter element"))

        l[i]=e
        print("Your updated list is now:\n")
        print(l)
else:
    print("Okay")
    
 

    
  


    