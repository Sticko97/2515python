

class Student:
    def __init__(self,name,student_id,grades=None):
        self.name=name
        self.student_id=student_id
        self.grades=grades
        if self.grades is None:
            self.grades = []
            
       
    def student_gpa(self):
        return sum(self.grades) / len(self.grades)
    
    def to_dict(self):
        return {
            "name":self.name,
            "student_id":self.student_id,
            "grades":self.grades
        }
    
    
    price = property(student_gpa)
        
        
    