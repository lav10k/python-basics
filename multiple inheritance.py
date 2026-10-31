class animal:
    def breed(self):
        print("carnivores")

class fox(animal):
    def fox(self):
        print("hello fox")
        
class tiger(animal):
    def tig(self):
        print("hello tiger ")
        
f=fox()
t=tiger()

t.breed()
t.tig()
f.fox()