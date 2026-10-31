class lav:
    def __init__(self, age):
        self.age=age
  
    def display(self):
        return "Hello"
        
    def display(self, age):
        print("Hello",age)
        
s=lav(20)
k=s.display()
s.display(20)

        
