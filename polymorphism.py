class sum:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def display(self,a,b):
        x=self.a+self.b
        print(x)
    def display(self,a,b,c):
        z=self.a+self.b+self.c
        print(z)
        

k=sum()
k.display(10,12,13)      