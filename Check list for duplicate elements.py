#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
'''
wap to check if a list contains any duplicat elements

logic

Take a list check its len 
convert the list to set (since set cannot contain duplicates the len of both will differ)
also when you convert a list with duplicate elements to set all the duplicates are ignored from set
'''

my_list=[1,2,3,4,4]  #you can input and store too logic remains same

if len(my_list)==len(set(my_list)):
    print("list contains no duplicates")
else:
    print("list has duplicates")


'''
output:
my_list=[1,2,3,4,4] 
list has duplicates

'''