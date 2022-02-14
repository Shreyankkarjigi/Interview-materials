#factorial
#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem: Wap to display factorial of a number

#logic
#no factorial for negative number
#factorial of 0 does not exist
#factorial of number is 1 to that number 
n=int(input("enter number"))

factorial=1

if n<0:
    print("sorry factorial does not exist")

elif n==0:

    print("factorial of 0 is 1")
else:

    for i in range(1,n+1):
        factorial=factorial*i
    print("factorial of num is",factorial)


  