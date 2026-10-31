class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def addition(self):
        add=self.a+self.b 
        return add
    
    def subtraction(self):
        sub=self.a-self.b 
        return sub
    
    def Multiplication(self):
        mul=self.a*self.b 
        return mul
    
    def Division(self):
        div=self.a/self.b 
        return div

print("Calculator")
print("1 Addition \n2 Subtraction \n3 Multiplication \n4 Division") 
z=int(input("Enter choice:"))       
a=int(input("Enter a Value:"))
b=int(input("Enter a value:"))
c=calc(a,b)

match z:
    case 1:
        print("Addition of",a,"and",b,"is :",c.addition())
    case 2:
        print("Subtraction of",a,"and",b,"is :",c.subtraction())
    case 3:
         print("Multiplication of",a,"and",b,"is :", c.Multiplication())
    case 4:
        print("Division of",a,"and",b,"is :",c.Division())
        
    

