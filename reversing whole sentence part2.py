
'''
return a string in reverse form with ',' removed and cases swapped

'''
s=str(input("Enter string"))

#convert the string into list using split()

l=s.split()

#reverse the string

r=l[::-1]

#use join method to convert list to string

string=' '.join(r)

#perform swapcase and print the string

print(string.swapcase())