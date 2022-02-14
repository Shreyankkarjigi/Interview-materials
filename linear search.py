#linear search
'''
give an array,containing n elements,our task is to find a given element in array and return its index if its present in array,else return -1

Time complexity: O(n)
'''
#implementation

def linear_search(sequence,n):

    for i in sequence:

        if i==n:

            return print("Element present at index",sequence.index(i))

    return -1

print(linear_search([1,2,3,4,5,6,7,8],4))


# output
'''
n=4
o/p=Element present at index 3
n=9
o/p=-1
'''