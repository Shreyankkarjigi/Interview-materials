#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
#input a string from user 
#input a index value from user
#input second string from user
#concat second string to first string at given index

'''
example

string1="shreyank"
string2="karjigi"
index=1

output=skarjigireyank 

index element is completely removed and replaced with second string
'''

string1=str(input("enter first string"))
string2=str(input("enter second string"))
index=int(input("enter index value"))

new_string=string1[0:index]+string2+string1[index+1:]
print(new_string)

'''
altenatively dont remove the char just add the string
skarjigihreyank
'''

new_string2=string1[0:index]+string2+string1[index:]
print(new_string2)


'''
output

enter first stringshreyank
enter second stringkarjigi
enter index value1
skarjigireyank
skarjigihreyank

'''