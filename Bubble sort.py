#Bubble sort algorithm (comparison based sorting)
#sorting with comparison algo
'''
In bubble sort,we compare and sort adajacent elements and are swapped, with smaller elements to left and larger element to right
This algo is not suitable for larger dataset as its worse case scenario is O(n2)

How bubble sort works in following manner:
consider an unsorted list
[14,33,27,35,10]
lets compare 14 and 33 first
14<33 ,so they are in correct position
next we compare
33 and 27
27<33
so we swap
[14,27,33,35,10]
next we compare 33 and 35
33<35 so no need to swap
next we compare 35,10
10<35
swap
[14,27,33,10,35]
iteation 1 ends here,but list isnt sorted yet
so we iterate again until 10 comes to right position
[10,14,27,33,35]
'''
#implementation

#define function,pass sequence as parameter

def bubble(sequence):

    #define range,this will till len of sequence-1 as we cant compare last element with anything

    r=len(sequence)-1

    #for now lets sorted=False,this wiil act as exit point in loop

    sorted=False

    #we use while loop , if list is already sorted , return list as it is 

    while not sorted:
        
        #sorted=true
        sorted=True

        #check each element in list,compare with adjacent element

        for i in range(r):

            if sequence[i]>sequence[i+1]:
                #set sorted as false
                sorted=False
                #swap
                sequence[i],sequence[i+1]=sequence[i+1],sequence[i]


    return sequence
#call function ,pass unsorted list as argument
print(bubble([14,33,27,35,10]))














