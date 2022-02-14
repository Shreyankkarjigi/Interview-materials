#program
#display most repeated number in list

'''
logic

repeated numbers are nothing but duplicates
a list can store duplicate but a set cannot store a duplicate

so somehow we have to display the most repeated number in the list

so first we convert the list into set (coz set cannot have duplicates),then we use max to count the max number of duplicates in list

'''

my_list=[1,2,3,4,5,6,7,8,9,9,9,9]
print(my_list)

most=max(set(my_list))
print(most)


'''
output
[1, 2, 2, 3, 4, 4, 2, 5, 5, 5, 5, 5]

5
'''