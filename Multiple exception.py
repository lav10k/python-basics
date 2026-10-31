#multiple exception
#This code attempts to convert list elements and handles ValueError, TypeError and IndexError.

a=[10,"twenty","30"]
try:
    total=int(a[0])+int(a[1])
except(ValueError,TypeError) as e:
    print("Error",e)
except IndexError:
    print("Out of index")

#output:  Error invalid literal for int() with base 10: 'twenty'