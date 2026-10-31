class teacher:
    def intro_teacher(self):
        print("hello, I am teacher!")

class student(teacher):
    def std_intro(self):
        print("hello, I am student!")
        
s= student()
s.intro_teacher()
s.std_intro()
        