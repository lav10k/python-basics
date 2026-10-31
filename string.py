#Creating string
s='hello from lav'
print(s,"\n")

#Multiline string (Using triple quotes""""....""")
k="""This is vs code
learning python """
print(k,"\n")

#Accessing Characters in String
l='hello world'
print(l[4])
print(l[8],"\n")

#String Slicing
j='lavkumardahake'
print(j[0:3])
print(j[3:8])
print(j[8:14],"\n")

#Looping Through Strings
s = "ABCDEF"
for char in s:
    print(char)

#String Immutability
s = "lavkumar"
s = "L" + s[1:]  
print("\n",s)

#updating string
s = "blue"
s1 = "M" + s[1:]                  
s2 = s.replace("blue", "clue")  
print("\n",s)
print(s1)
print(s2,"\n")

#String Methods

#len()
s='lavkumar'
print(len(s),"\n")

#upper() lower()
print(s.upper())
s="HELLO"
print(s.lower())

#Deleting string
del s

#strip() and replace()
s="    PYTHON        "
print("\n",s)
print(s.strip())

s="virat kholi"
print(s)
print(s.replace("virat","king"))

#Concatenating and Repeating Strings

#concatenating
s1="lav"
s2="dahake"
print("\n",s1+"kumar"+s2)

#Repeating string
s="hello"
print("\n",s*3)

#Formatting Strings
#1 Using f-strings
name = "lav"
age = 20
print(f"\n Name: {name}, Age: {age}")

# 2 Using format()
s = "\n My name is {} and I am {} years old.".format( "lav", 20)
print(s)

#String Membership Testing
s = "virat kholi"
print("virat" in s)
print("king" in s)