n=int(input("Enter a number:"))
try:
    res=n/0
except ZeroDivisionError:
    print("Can not be divided by Zero")
    