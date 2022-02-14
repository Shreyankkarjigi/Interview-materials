#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
'''
wap to check if two entered strings are anagrams.
a string is said to be anagram if letters of one word can be rearanged to form other word.Example "jaxa" and "ajax" are anagram of each other

'''
'''
logic

Take two strings from user , split the letters of both strings into two separate lists
compare both lists if they are same they are anagram else they are not
'''
x=str(input("Input string 1\n"))
y=str(input("Input string 2\n"))

my_list=[]
my_list1=[]
for i in x:
    my_list.append(i)
    #sort the list as letters need to be in same sequence in both lists
    my_list.sort()

for j in y:
    my_list1.append(j)
    my_list1.sort()


if my_list==my_list1 or my_list1==my_list:
    print("Its an anagram")
else:
    print("Its not an anagram")

'''
output

Input string 1        #execution
ajax                  #list1 formed as['a','j','a,'x']
Input string 2        #list1 got sorted as ['a','a','j','x']
jaxa                  #list2 formed as['j','a','x','a']
Its an anagram        #list2 got sorted as ['a','a','j','x']
                      #both sorted list got compared if they are equal its in an anagram else not

                      #why sorting was required

                      when comparing lists compare element to element or index to index

                      so both index in both lists should have the same value in it.


'''