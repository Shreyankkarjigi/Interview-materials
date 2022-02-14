#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
#add chars to list

#init a list to store elements(chars)
my_chars=[]

#first take range of elements from user

n=int(input("enter range"))

#iterate over that range and ask user to input elements

for i in range(n):
    x=str(input("Enter characters"))

    #append it to list
    my_chars.append(x)

    #print the list

print(my_chars)


'''
output

enter range2
Enter charactersa
Enter charactersb
['a', 'b']

'''