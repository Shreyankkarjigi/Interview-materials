#Binary search algorithm
'''
performed on sorted array,
goal of this algorithm is to search an element in sorted element by comparing it with middle element

How it works:

we assign lower (first element) and upper(last element) in array
Next we find middle point of the array

Then we compare the element to be searched with middle element

case1: If element==middle value, return index of mid element

case2: If element<middle (element smaller than mid element),search shifts to right of middle element

we change the upper point to mid-1(shifts search to right of mid)

case3: If element<middle (element greater than mid element),Iteration shifts to left of middle element

we change the lower point to mid+1(shifts search to left of mid)
'''
#implementation

#define a function which takes sorted list and item to be searched as parameters

def binary_search(list_a,item):

    #define lower and upper bounds
    #lower will be always index 0 so we say lower=0
    lower=0
    #upper will be aleways last element of list,so we do this by len(list)-1
    upper=len(list_a)-1

    #The iteration will continue until lower bound is less or equal to higher bound

    while lower<=upper:

        #initate mid point,using formula
        mid_point=lower+(upper-lower)//2

        #extract mid value using mid_point
        mid_value=list_a[mid_point]

        #cases

        if item==mid_value:
            #return mid_point
            return print("Element at index:",mid_point)


        #if item is smaller than mid_value,change upper=mid-1

        elif item<mid_value:
            upper=mid_value-1

        #else item is higher than mid_value.change lower=mid+1
        else:

            lower=mid_value+1


    return None


print(binary_search([2,3,4,5,6,7,8],4))

'''
output
Element at index: 2
'''




