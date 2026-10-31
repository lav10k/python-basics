#Catch-All Handlers and Their Risks
#dividing a string by a number, which causes a TypeError.

try:
    # Risky operation: dividing string by number
    res="100"/20 
except ArithmeticError:
    print("Arithmetic problem.")
except:
    print("Something went wrong!")