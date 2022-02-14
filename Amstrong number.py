#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#Amstrong code 

#take number input

n=int(input("enter number"))

#store input in temporary variable

temp=n

#initaliaze a sum variable set it to 0

sum=0

#run a while loop until temp in greater than 0

while temp>0:

    #separate digits using %10 method

    digit=temp%10

    #add sum + digts cube

    sum=sum+digit**3

    #divide orignal number by 10

    temp=temp//10



#check if sum==orignal number 


if sum==n:
    print("is amstrong")

else:
    print("not an amstrong")