#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
'''
Sorting list of your 10 bestfriends 

Take names from user

'''

my_friends=[]

for i in range(1,11):
    print(i)
    names=str(input("Enter name of your friend"))
    
    my_friends.append(names)
    my_friends.sort()

print(my_friends)

'''
output

1
Enter name of your friendabhay
2
Enter name of your friendrishabh
3
Enter name of your friendsneha
4
Enter name of your friendaditya
5
Enter name of your friendkedar
6
Enter name of your friendviraj
7
Enter name of your friendrishi
8
Enter name of your friendsrushti
9
Enter name of your friendtanya
10
Enter name of your friendsunny
['abhay', 'aditya', 'kedar', 'rishabh', 'rishi', 'sneha', 'srushti', 'sunny', 'tanya', 'viraj']

'''