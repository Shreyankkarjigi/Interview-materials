#factorial of a number
#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem: Wap to display factorial of a number


n=int(input("enter number:\n"))

factorial=1

#check conditons

#.factorial of 0 is 1
#no factotrial of negative number


if n==0:

    print("factorial of 0 is 1")

elif n<0:
    print("factorial of negative number doesnt exist")


else:

    for i in range(1,n+1):

        factorial=factorial*i

    print("factorial of",n,"is",factorial)


#output
'''
enter number:
7
factorial of 7 is 5040

'''