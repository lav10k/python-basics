def rect():
    l=int(input("Enter Length: "))
    b=int(input("Enter breadth: "))
    print("Area of Rectangle: ",l*b)

def square():
    s=int(input("Enter side of square: "))
    print("Area of square: ",s*s)
    
def circle():
    r=int(input("Enter Radius: "))
    pie=3.14
    cir=pie*r*r
    print("Area of circle: ",cir)
    
def triangle():
    h=int(input('Enter height of triangle: '))
    b=int(input('Enter base of triaangle: '))
    tri=(h*b)/2
    print("Area of triangle: ",tri)
    
print("Area")
print("1 Area of rectangle")
print("2 Area of Square")
print("3 Area of Triangle")
print("4 Area of Circle")

x=int(input('Enter a choice (1-4):'))
match x:
  case 1:
      print("Area of Rectangle")
      rect()
  case 2:
      print("Area of Square")
      square()
  case 3:
      print("Area of Triangle")
      triangle()
  case 4:
      print("Area of Circle")
      circle()
      
   


    