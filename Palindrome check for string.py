#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem: Wap to display fibonacci series

#input string from user

string=str(input("Enter string:\n"))

#def function and pass string as argument

def Palindrome(string):

    #use slicing method to check 

    if string[::-1]==string:
        print("It is a palindrome")

    else:
        print("It is not a palindrome")

Palindrome(string)

'''
output
Enter string:
shreyank

It is not a palindrome

mom
It is a palindrome
'''