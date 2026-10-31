a=[1,2,3] #list created using square brackets[]
print(a[2]) #output 3
print(a) #output[1,2,3]

#list can store any data type int, float, string

b=['hello',1,4.56]
print(b) #output['hello',1,4.56]

#Using list() Constructor

a=list(('xyz',4,5,6.7)) # list() function
print(a)   #output['xyz', 4, 5, 6.7]

b=list(("lav"))  #list store string as individual character
print(b)   #output ['l', 'a', 'v']

#Creating List with Repeated Elements
a=[2]*4
b=[4,5,7]*8 
print(b)  #output [4, 5, 7, 4, 5, 7, 4, 5, 7, 4, 5, 7, 4, 5, 7, 4, 5, 7, 4, 5, 7, 4, 5, 7]
print(a)  #output [2, 2, 2, 2]

#Accessing Elements
a=[18,7,2006]
print(a[0])  #output 18
print(a[-1])  #output 2006

### FUNCTIONS OF LISTS ###
# adding element: 

# append() function
a = [1, 2]
a.append(3) #element is stored in last 
print(a)  #output [1, 2, 3]

#insert(): Adds an element at a specific position.
a=[4,5,6,7]
print(a) #output [4, 5, 6, 7]
a.insert(3,9) # 3 is the position and 9 is element
print(a)  #output [4, 5, 6, 9, 7]

#extend([]): Adds multiple elements to the end of the list.
a=[1,2]
a.extend([3,4])
print(a) #output [1, 2, 3, 4]

#remove(): Removes the first occurrence of an element.
a = [1, 2, 3]
a.remove(2)
print(a)

#UPDATING ELEMENT#
a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)  #output [10, 25, 30, 40, 50]

### Removing Elements ###
 
#pop() removes the element from specific index or the last element if no index is given
a = [1, 2, 3]
a.pop(2)
print(a) #output [1, 2]

b=[2,3,4,5,6]
b.pop()
print(b) #output [2, 3, 4, 5]




