#Quicksort Algorithm (Sorting algorithm)
'''
#quicksort works on unsorted sequence and sorts it in either ascending or descending order
#we select a pivot point and compare all elements with pivot
#if number is less than pivot,it goes to right of pivot 
#if number is great than pivot,it goes to left of pivot
#we repeat this until entire sequence is in proper sequence
#if len of sequence is less than or equal to 1 ,we return the sequence as it is,as list contatining single item are already sorted
Time complexity of quicksort is O(nlogn) (best case) and O(n)(worst case)
'''
#implementation
#define function,pass sequence as parameter                                                                                            
def quicksort(sequence):
    #if len of sequence less than or equal to 1,return sequence
    if len(sequence)<=1:
        return sequence
    else:
        #declare pivot,i chose last element as pivot
        pivot=sequence.pop()
    #declare two lists,one to hold items lesser than pivot and one to hold greater than pivot
    item_lower=[]
    item_greater=[]
    #initalise a for loop to iterate over each element as compare each element with pivot and append to respective lists
    for i in sequence:
        if i<pivot:
            #if element is smaller than pivot,append to item_lower list
            item_lower.append(i)
            #else append to item_greater list
        else:
            item_greater.append(i)
    #return sequence while applying quicksort again to both lists and also concat it with pivot
    return quicksort(item_lower)+[pivot]+quicksort(item_greater)
#call function ,pass an unsorted sequence
print(quicksort([5,4,1,7,9,3]))    

'''
#Example run

5,4,1,7,9,3
          Pivot

1.compare 5,4,1 with pivot 

5>3,goes right of pivot,appended to item_greater list
4>3,goes right of pivot,appended to item_greater list
1>3,goes left of pivot,appended to item_lower list
7>3,goes right of pivot,appended to item_greater list
9>3,goes right of pivot,appended to item_greater list

so both list have following content

item_lower=[1]
item_greater=[5,4,7,9]

notice how item greater isnt sorted yet,so while returning we again applied quick sort on it
so after re running algo on both lists we get following

item_lower=[1]
item_greater=[4,5,7,9]

next we return the sorted list with pivot in middle
following sorted list will be returned

[1,3,4,5,7,9]
   p
   
'''  
 



