#Specific Exception
#This code handles ValueError and ZeroDivisionError with different messages.
try:
    #value error
    x=int("str")
    inv=1/x  
except ValueError:
    print("Not valid")
except ZeroDivisionError:
    print("Can not divide by zero")      