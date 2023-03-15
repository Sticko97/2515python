import csv 

class Student:
    def __init__(self, name,  student_id, grades):
        """ Constructor - Initializes the main attributes of a student """
        self._name = name
        self._student_id = student_id
        self._grades = grades
        
    def compute_average_grade(self):
        """Returns average grade"""
        return sum(self._grades) / len(self._grades)
    
class School:
    def __init__(self):
        """ Constructor - Initializes the main attributes of School """
        self._students = []
        with open("students.csv", "r") as file:
            student_csv = csv.DictReader(file)
            for row in student_csv:
                name = row["name"]
                student_id = row["student_id"]
                grades = []
                with open("grades.csv", "r") as gradeFile:
                    grade_csv = csv.reader(gradeFile)
                    for grade_row in grade_csv:
                        if grade_row[0] == student_id:
                            grades.append(float(grade_row[1]))
                self._students.append(Student(name, student_id, grades))
                        

    def find_students_by_name(self, name):
        """Takes string name and returns list of Student whose name is equal"""
        found_students = []
        for student in self._students:
            if student._name == name:
                found_students.append(student)
        return found_students
    
    
    def find_students_by_id(self, student_id):
        """Takes string id and returns list of Student whose id is equal"""
        studentID = []
        for student in self._students:
            if student._student_id == student_id:
                studentID.append(student)
        return studentID
    
    def print_student_list(self, full=False, sort=None):
        """prints a list on the screen showing all students with their name, student ID and average grade"""
        if sort == "name":
            self._students.sort(key=lambda x: x._name)
        elif sort == "id":
            self._students.sort(key=lambda x: x._student_id)
        elif sort == "average":
            self._students.sort(key=lambda x: x.compute_average_grade())
            
        for student in self._students:
            print("Name:", student._name)
            print("Student ID:", student._student_id)
            print("Average grade:", student.compute_average_grade())
            if full:
                print("Grades:", student._grades)
            print("\n")

if __name__ == '__main__':
    school = School()
    print("Full student list:")
    school.print_student_list(full=True, sort='name')
    print("\nStudent list sorted by average grade:")
    school.print_student_list(sort='average')
    print("\nStudent list sorted by ID:")
    school.print_student_list(sort='id')



