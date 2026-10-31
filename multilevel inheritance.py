class animal:
    def breed(self):
        print("king lion (grand father)")
    
class lion(animal):
    def lion(self):
        print("lion (father)")
        
class cub(lion):
    def cub(self):
        print("cubs (child)")
        
c=cub()
c.breed()
c.lion()
c.cub()