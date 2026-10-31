#Raise an Exception
#raise keyword
#Syntax: raise ExceptionType("Error message")

#ValueError if an invalid age is given.
def set(age):
    if age<0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")
try:
    set(-4)
except ValueError as e:
    print(e)