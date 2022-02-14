#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem: 
#Wap to input string from user , check for vowels , if vowels are present in string then add them to a separate list  and print that list.
#print the total number of vowels in string.
#prints the string with all the vowels removed from it.

#solution

#initate a input for string

string=str(input("Enter a string:\n"))

#initate a vowel list

vowel=['a','e','i','o','u']

#initate another list to store the vowels formed in that string

vowels_found=[]

#def a function,pass string,vowel list and vowel_found list as argument

def vowel_check(string,vowel,vowels_found):

    #iterate over string and check if element of list vowel are present in it
    #convert the string to lower case before execution

    for i in string.lower():
        if i in vowel:

            #store the found vowels in vowel_found list

            vowels_found.append(i)

            #use another if statement to remove the found vowels from the string

        if i in vowels_found:

            string=string.replace(i,"")

    #finally print out everything in sequence

    print("Found Total:\n",len(vowels_found))
    print(vowels_found)
    print("String after vowel removed from it:\n")
    print(string)




#call function,pass the same arguments

vowel_check(string,vowel,vowels_found)



#output generated 
'''
Hi My name is Shreyank and I am a Dumb Coder
Found Total:
 13
['i', 'a', 'e', 'i', 'e', 'a', 'a', 'i', 'a', 'a', 'u', 'o', 'e']
String after vowel removed from it:

H My nm s Shrynk nd I m  Dmb Cdr
'''
