#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
#take elements from user add it to list
#init a list to store elements(numbers)
my_numbers=[]

#first take range of elements from user

n=int(input("enter range"))

#iterate over that range and ask user to input elements

for i in range(n):
    x=int(input("Enter numbers"))

    #append it to list
    my_numbers.append(x)

    #print the list

print(my_numbers)


'''
output
enter range2
Enter numbers1
Enter numbers2
[1, 2]
'''