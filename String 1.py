#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
'''
problem: Wap to take full name as input in form of first name , middle name , last name
and print in follwing format 
example Input:- robert downey juniour
output: R.D.Juniour.

'''


'''
take first name ,middle name,last name as input
'''

first=str(input("Enter first name\n"))

middle=str(input("Enter middle name\n"))

last=str(input("Enter last name\n"))

'''
One line solution 
use title() to capitalize first letter of word
'''

print("Your name is\n",first[0].title()+"."+middle[0].title()+"."+last.title()+".")


'''
output

Enter first name
robert
Enter middle name
downey
Enter last name
jr
Your name is
 R.D.Jr.
 
'''