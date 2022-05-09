

class Student():
    
    #Construcor
    def __init__(self, n, r):
        self.name = n
        self.roll = r
    
    #Instance Method
    def disp(self):
        print("Student Name : ", self.name)
        print("Student Roll : ", self.roll)
        

class User():
    

    #Static Method
    @staticmethod
    def show(s):
        print("Student Information : ")
        print(s.name)
        print(s.roll)
    

stu = Student("Malik", 865)
User.show(stu)