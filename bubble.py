#Quicksort(Unsorted)

def Quicksort(sequence):

    #if len is less or equal to 1 ,it is already sorted

    if len(sequence)<=1:
        return sequence

    else:
        #set pivot

        pivot=sequence.pop()
        great=[]
        less=[]

        for i in sequence:

            if i>pivot:
                #great

                great.append(i)

            else:

                less.append(i)


        return Quicksort(less)+[pivot]+Quicksort(great)


print(Quicksort([0,4,3,2,5,1]))

