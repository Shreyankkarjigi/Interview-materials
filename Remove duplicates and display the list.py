#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
'''
You have a list of items containing lot of duplicates in it.Your task is to make a new list where all the duplicates have been removed , also from the original list display the most repeated number.

sample input
[1,2,3,4,5,5,5,5,6,6,7,7,7]

sample output

[1,2,3,4,5,6,7]

most repeated item is: 5
'''
#For sake of less code i considered a predefinend list , you can also ask user and add to list

my_list=[1,2,3,4,5,5,5,5,6,6,7,7]

print("Here is my original list\n")
print(my_list)

# serach most repeated number in list , for this convert the list to set and count max duplicates
# why use key and count?

#


most_rep=max(set(my_list),key=my_list.count)

print("Most repeated number in list is:",most_rep)


#remove the duplicates from list , to do this simply convert the list to set as set cannot contain any duplicates

new_list=set(my_list)

print("List without duplicates\n")
print(new_list)