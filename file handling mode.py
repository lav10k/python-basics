#read mode "r"
with open('G:\python\hello world.txt', 'r') as file:
    content = file.read()
    
# Write mode "w"
with open('G:\python\hello world.txt', 'w') as file:
    file.write('Hello, world!')
    
#append mode "a"
with open('G:\python\hello world.txt', 'a') as file:
    file.write('\nThis is a new line.')
    
#binary mode "b"
with open("G:\python\IMG20220810173841 (1).jpg", 'rb') as file:
    data = file.read()
    print(data)
    # Process the binary data

