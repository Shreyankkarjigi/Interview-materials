#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem: Wap to display fibonacci series

#take range input from user

n=int(input('enter range'))

#define function,pass range as argument

def Fibo(n):
    #intialize a=0 and b=0

    a=0
    b=1
    #print a and b
    print(a)
    print(b)

    #initalize for loop of range n

    for i in range(n):
        #initalize c=a+b and swap values of a,b,c

        c=a+b
        a,b=b,c
        print(c)

#run function

Fibo(n)

'''
output

enter range5
0
1
1
2
3
5
8

'''