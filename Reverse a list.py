#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
'''
input a list from user print in reverse order without using reverse function

'''
my_list=[]

#input range

n=int(input("Enter range"))

for i in range(n):

    num=int(input("Enter numbers"))

    my_list.append(num)

print(my_list[::-1])


'''
output

Enter range5
Enter numbers1
Enter numbers2
Enter numbers3
Enter numbers4
Enter numbers5
[5, 4, 3, 2, 1]

'''

    
    