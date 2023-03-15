import csv

class Student:
    def __init__(self, name, student_id, grades):
        """ Constructor - Initializes the main attributes of a student """
        self.name = name
        self.student_id = student_id
        self.grades = grades

    
    def student_average_grade(self):
        """Returns average grade"""
        return sum(self.grades) / len(self.grades)
    
class School:
    def __init__(self):
        """ Constructor - Initializes the main attributes of School """
        self.name_list = []
        grade_list=[]
        with open("students.csv", "r") as f:
            student_file = csv.reader(f)
            next(student_file) # skips the field names/ first row
            for row in student_file:
                student_name = row[0]
                student_id = row[1]
                self.name_list.append(student_name)
                with open("grades.csv", "r") as g:
                    gradez = csv.reader(g)
                    for item in gradez:
                        if item[0] == student_id:
                            grade_list.append(item[1:])
        student = Student(student_name, student_id, grade_list)
        self.name_list.append(student)
                            
    def find_students_by_name(self, name):
        """Takes string name and returns list of Student whose name is equal"""
        matched_students = []
        for stu in self.name_list:
            if stu.lower() == name.lower():
                matched_students.append(stu)
        return matched_students
    
    def find_students_by_id(self, student_id):
        """Takes string id and returns list of Student whose id is equal"""
        matched_id = []
        for id in self.student_name_list:
            if id == student_id:
                matched_id.append(id)
        return matched_id
    

    # def print_student_list(self, full=False, sort=None):
        '''prints a list on the screen showing all students with their name, student ID and average grade'''
        
        
        
            
    
            


                            
    
    
                
      
                    
                            
                            
                    
                
                # with open("grades.csv", "r") as file:
                #     grade_file = csv.reader(f)
                #     for item in grade_file:
                #         if item == name:
                #             name_list.append[item]
                #         elif item == student_id:
                #             name_list.append[item]
                #     print(name_list)
'''splits firstname from lastname'''
# import csv
# list = []
# with open("students.csv", "r") as file:
#     student = csv.reader(file)
#     for row, let in student:
#         a = row.split()
#         print(a)
    
    
# with open("grades.csv", "r") as gradeFile:
#     grade = csv.reader(gradeFile)
#     for row in grade:
#         print(row[0])

# with open("students.csv", "r") as studentFile:
#     student = csv.DictReader(studentFile)
#     for row, let in student:
#         a = row.split()
#         print(a)