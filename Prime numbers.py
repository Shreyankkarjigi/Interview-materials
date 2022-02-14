#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
#Prime number check

num=int(input("Enter number"))

if num>1:

    for i in range(2,num):
        if (num%i)==0:
            print('Not prime')
            break

        else:
            print("Prime number")
            break

else:
    print("Not a prime")




'''
output
Enter number11
Prime number


'''
    

