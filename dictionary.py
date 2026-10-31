#creating a dictionary
a={"x":1,"y":2}
print(a) #output: {'x': 1, 'y': 2}
#dict() function
b=dict(name="lav",age=20)
print(b) #output: {'name': 'lav', 'age': 20}

#Accessing Dictionary items

d={"name":"lav","age":20}
print(d["name"]) #output: lav
print(d["age"])  #output: 20

#adding and updating dictionary item

d={"name":"virat kholi"}
d["number"]=18  # Adding a new key-value pair
d["name"]="king"# Updating an existing value
print(d) #output:{'name': 'king', 'number': 18}

#removing Dictionary items

#1 del: removes an item using its key

d={"a":1,"b":2}
del d["a"]
print(d)#output:{'b': 2}

#2 pop(): removes the item with the given key and return its value

d={"a":1,"b":2}
val=d.pop("a")
print(val) #output: 1
print(d)   #output: {'b': 2}

#3 popitem(): removes and returns the last inserted key-value pair

d = {"a": 1, "b": 2}
print(d.popitem())   #output: ('b', 2)

#4 clear(): removes all items from the dictionary

d = {"a": 1, "b": 2}
d.clear()
print(d)  #output: {}

#Iterating Through a Dictionary

#1  Iterate keys: Returns all keys from the dictionary.
d = {"a": 1, "b": 2}
for key in d:
    print(key)  #output: a
                #        b

#2 Iterate values: Returns all values from the dictionary.

d = {"a": 1, "b": 2}
for value in d.values():
    print(value)
#output:
 #  1
 #  2 

#3. Iterate key-value pairs: Returns all key-value pairs as tuples.

d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)
    
#output:
#a 1
#b 2

#Nested Dictionaries
d = {
    "student": {
        "name": "lav",
        "age": 20
    }
}

print(d["student"]["name"])

#output:lav