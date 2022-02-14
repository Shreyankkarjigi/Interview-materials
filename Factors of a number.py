#factors
#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem: Wap to display factors of a number
#factors of number show all the numbers by which the number can be divided.


n=int(input("enter number:\n"))

for i in range(1,n+1):
    if n%i==0:
        print(i)


'''
output
enter number:
320
1
2
4
5
8
10
16
20
32
40
64
80
160
320
'''