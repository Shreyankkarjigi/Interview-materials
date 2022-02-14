#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem

'''
compare two lists print out common in another list
'''


list_a=[1,2,3,4]
list_b=[2,3,4,5]
common=[]

for i in list_a:
    for j in list_b:
        if i==j:
            common.append(i)

print(common)

'''
output
[2, 3, 4]
'''