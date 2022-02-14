#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
'''
Wap to make a new string with the word "The" removed from the string

"This is the lion in the cage"

'''

string="This is the lion in the cage"

#safe side convert the string to lowercase
string.lower()
#use replace function
string_new=string.replace("the","")

#print the new string

print(string_new)



'''
output

This is  lion in  cage
'''