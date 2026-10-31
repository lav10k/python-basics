s={1,2,3,4}
print(s)  #output: {1, 2, 3, 4}

#set() function
s= set()
print(s) #output:  set()

s= set("lavkumar")
print(s) #output: {'l', 'k', 'a', 'm', 'u', 'r', 'v'}

#creating a set with the use of a list
s=set(["hello","world","LAV!"])
print(s)  #output: {'hello', 'world', 'LAV!'}

#creating a set with use of a tuple
t=("lav","Kumar","Dahake")
print(set(t)) #OUTPUT: {'Kumar', 'Dahake', 'lav'}

# Creating a Set with the use of a dictionary
d = {"Lav": 1, "KUMAR": 2, "dahake": 3}
print(set(d)) #output: {'KUMAR', 'Lav', 'dahake'}

# Unordered, Unindexed and mutability

s={3,1,4,1,5,9,2}
print(s)  #output: {1, 2, 3, 4, 5, 9}
try:
     print(s[0])
except TypeError as e:
    print(e)  #output: 'set' object is not subscriptable
    
#Adding elements to a set
# add() method , update() method
s={1,2,3,4}
s.add(5)
s.update([5,6])
print(s)  #output: {1, 2, 3, 4, 5, 6}

#Accessing a set

s={"lav","hello","lav"}
for i in s:
    print(i, end=" ") #output: lav hello 
print("\n","lav" in s) #output: True

#Removing Elements from the set
#using remove() Method or discard()method

s={1,2,3,4,5,60}
s.remove(60)
print(s) #output: {1, 2, 3, 4, 5}

s.discard(4)
print(s) #output: {1, 2, 3, 5}

# using pop() Method
s={1,2,3,4,5,6}
val=s.pop()
print(val) #output: 1
print(s) #output: {2, 3, 4, 5, 6}

#using clear() method
s={1,2,3,4,5}
s.clear()
print(s) #output: set()

# frozenset
fs= frozenset([1,12,3,4,5])
print(fs) #output: frozenset({1, 3, 4, 5, 12})
s={1,2,3,3,45,68,8}
fs=frozenset(s)  
print(fs) #output: frozenset({1, 2, 3, 68, 8, 45})

#typecasting object into sets

li=[1,1,2,3,4,5,2,5,7]
s=set(li)
print(s) #output: {1, 2, 3, 4, 5, 7}

s = "lavkumar"
s = set(s)
print(s) #output: {'v', 'm', 'a', 'u', 'r', 'k', 'l'}

d = {1: "One", 2: "Two", 3: "Three"}
s = set(d)
print(s) #output: {1, 2, 3}