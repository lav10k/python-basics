try:
    file=open("G:\python\hello world.txt", "r")
    content=file.read()
    print(content)
except FileNotFoundError as e:
    print("Error:",e)
finally:
    file.close()