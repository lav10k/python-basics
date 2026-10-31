class student:
    def __init__(self, rollno, name, Class):
        self.rollno = rollno
        self.name = name
        self.Class = Class


class Marksheet(student):
    def __init__(self, rollno, name, Class):
        student.__init__(self, rollno, name, Class)
        self.total = 0
        self.percentage = 0

    def marksheet(self):
        print("\nEnter Marks")
        eng = int(input("English: "))
        maths = int(input("Maths: "))
        cs = int(input("CS: "))
        gk = int(input("General Knowledge: "))

        self.total = eng + maths + cs + gk
        self.percentage = (self.total * 100) / 400


class Display(Marksheet):
    def display(self):
        print("\nMARKSHEET")
        print("Roll No :", self.rollno)
        print("Name    :", self.name)
        print("Class   :", self.Class)
        print("Total   :", self.total)
        print("Percentage :", self.percentage, "%")

        if self.percentage >= 36:
            print("Result : Passed")
        else:
            print("Result : Fail")


n = int(input("Enter number of Students: "))

for i in range(n):
    print("\nStudent", i + 1)
    rollno = input("Enter Roll No: ")
    name = input("Enter Name: ")
    Class = input("Enter Class: ")
    d = Display(rollno, name, Class)
    d.marksheet()
    d.display()
        
    
 
     
  
