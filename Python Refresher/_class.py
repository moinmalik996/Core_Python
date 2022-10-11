# class Student:
    
#     def __init__(self):
#         self.name = 'Malik'
#         self.age  = 25


# stu1 = Student()
# print(stu1.name)
# print(stu1.age)


class Student:
    
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
    def average(self):
        return (sum(self.grades) / len(self.grades))
    
    
stu = Student('Moin Malik', (1, 2, 3, 4, 5))
print(stu.average())

    