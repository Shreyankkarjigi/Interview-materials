#sets
'''
denoted by {}
ordered 
mutable
indexed
support multiple data types
no duplicates


operations on sets:
1.Add
2.update
3.delete
4.Access elements
5.slicing 
6.striding
7.concat
8.Iterable


mathematical operations on sets

1.Union (|) - combine both sets,ignores duplicate elements
2.Intersection(&) - Common elements in both sets,ignores duplicat elements
3.Difference(-) - gets elements that are in set 1 but not in other set
4.Symmertic difference(^)- gets un-common elements in both sets

'''

#Initalizing a set
set1={1,2,3,4,6}
set2={1,2,3,4,5}

#1Union(|)

print(set1|set2)

#output:{1, 2, 3, 4, 5,6}

#Intersection(&)

print(set1 & set2)
#output:{1, 2, 3, 4}

#Difference(-)
#output:

print(set1-set2)

#output:{6}

#Symmetric difference

print(set1^set2)

#output:{5,6}


'''
Adding elements to set

1. using add method

'''
set1.add(8)
print(set1)

#output:   
#{1, 2, 3, 4, 6, 8}

#Adding multiple values to sets,using update(values),note: we pass values in a list

set1.update([9,10,11])
print(set1)
#output:{1, 2, 3, 4, 6, 8, 9, 10, 11}

#Remove values from set using remove(element)

set1.remove(11)
print(set1)
#output:{1, 2, 3, 4, 6, 8, 9, 10}


