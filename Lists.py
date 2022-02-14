#Lists
'''
denoted by []
ordered 
mutable
indexed
support multiple data types
allows duplicates
more memory consumption than array

operations on Lists:
1.Add
2.update
3.delete
4.Access elements
5.slicing 
6.striding
7.concat
8.Iterable

'''
#Adding to lists

#1.using append(adds at end)
'''
append adds at end of the list

'''
l=[1,2,3]
l.append(4)
print(l)

#output-[1, 2, 3, 4]

#2.add anywhere
#use insert
#insert(indexvalue,value)

l.insert(5,"a")
print(l)
#output-[1, 2, 3, 4, 'a']

#updating elements
#indexmethod
#list_name[index]=new_value
l[2]=7
print(l)
#output-[1, 2, 7, 4, 'a']

#deletion 
#1.using pop()
#removes last element by default 
l.pop()
print(l)

#2.using pop to remove any element
#pop(index)
l.pop(1)
print(l)

#using removing(char)
l.remove(1)
print(l)

#sorting lists
#1.sort lists using sort()
#sort() sorts the list ascending by default.
l1=[1,2,43,54,32,2]
l1.sort()
print(l1)
#output-[1, 2, 2, 32, 43, 54]

#sort(reverse=True),sorts in descending order
l1.sort(reverse=True)
print(l1)
#output-[54, 43, 32, 2, 2, 1]
