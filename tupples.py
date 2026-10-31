tup=()
print(tup)

#using string
tup=("hello, lav!")
print(tup)   #output: hello, lav!

#using list
li=[1,2,3,4,5]
print(tuple(li)) #output: (1,2,3,4,5)

#using built in function
tup= tuple("hello")
print(tup) #output: ('h', 'e', 'l', 'l', 'o')

#Creating a Tuple with Mixed Datatypes
tup=(1,4.5,"hello",2+6j)
print(tup) #output: (1, 4.5, 'hello', (2+6j))

#tuple basic operation
tup=("hello world")
print(tup[:4])  #output:hell
print(tup[0:7]) # hello w
print(tup[6:])  # world

#tuple unpacking

tup=("lav","kumar","dahake")
a,b,c=tup  #output:
print(a)   #lav
print(b)   #kumar
print(c)   #dahake

#concatenation of tuple
tup1=("virat", "kholi")
tup2=(1,8)
tup3= tup2 + tup1
print(tup3) #output: (1, 8, 'virat', 'kholi')

#slicing of tuple
tup= tuple("lavkumardahake")
print(tup[0:]) #('l', 'a', 'v', 'k', 'u', 'm', 'a', 'r', 'd', 'a', 'h', 'a', 'k', 'e')
print(tup[7:9]) #('r', 'd')
print(tup[::-1]) #('e', 'k', 'a', 'h', 'a', 'd', 'r', 'a', 'm', 'u', 'k', 'v', 'a', 'l')

#del tupel

tup=(1,2,3,4)
del tup

#Tuple Unpacking with Asterisk (*)
tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  #5