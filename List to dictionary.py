#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
'''
input two lists from user one is key and one is value
convert the lists into dictionary

logic
input two lists
use zip function to combine both lists
use dict() function
'''

list_keys=[]
list_values=[]

r=int(input("Enter range"))

for i in range(r):
    keys=input("Enter keys")
    values=input("Enter values")

    list_keys.append(keys)
    list_values.append(values)


print("Dictionary formed\n")
print(dict(zip(list_keys,list_values)))

'''
output
Enter range5
Enter keys1
Enter values22
Enter keys2
Enter values33
Enter keys3
Enter values44
Enter keys4
Enter values55
Enter keys5
Enter values66
Dictionary formed

{'1': '22', '2': '33', '3': '44', '4': '55', '5': '66'}

'''
