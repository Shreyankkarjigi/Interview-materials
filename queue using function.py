#queue using function
'''
queue are abstract data structure that uses a two way list to enter and remove elements

in que elements are entered from one side and removed from other side, it is based on FIFO (First in,first out) approach


push() is used to add elements to queue
pop() is used to remove elements from queue

queue is implemented using deque which is imported from collections module
'''

from collections import deque

queue=deque([])

#push function

def push(queue):

    for i in range(10):

        print("pushing element",i,"to queue")
        queue.append(i)

    print(queue)

def pop(queue):

    for j in range(10):

        print("removing element",queue.popleft(),"from queue")


    print(queue)

    if not queue:
        print("queue is now empty")


print(push(queue))
print(pop(queue))




'''
output

pushing element 0 to queue
pushing element 1 to queue
pushing element 2 to queue
pushing element 3 to queue
pushing element 4 to queue
pushing element 5 to queue
pushing element 6 to queue
pushing element 7 to queue
pushing element 8 to queue
pushing element 9 to queue
deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
None
removing element 0 from queue        
removing element 1 from queue        
removing element 2 from queue        
removing element 3 from queue        
removing element 4 from queue        
removing element 5 from queue        
removing element 6 from queue        
removing element 7 from queue        
removing element 8 from queue        
removing element 9 from queue        
deque([])
queue is now empty
None

'''