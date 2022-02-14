#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
'''
calculate simple intrest 

formula SI=(p*t*r)/100

p=principle amount
r= rate 
t= time
'''

p=int(input("input principle amount\n"))
r=int(input("input rate\n"))
t=int(input("enter time\n"))
si=""
def simple_int(p,r,t,si):

    si=(p*r*t)/100
    print("simple intrest is:",si)
simple_int(p,r,t,si)



'''
output
input principle amount
10000
input rate
5
enter time
5
simple intrest is: 2500.0

'''




