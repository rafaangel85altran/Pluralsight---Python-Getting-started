'''
Created on 23 may. 2018

@author: win7
'''

#Example of nested function

def get_students():
    
    students = ["mark", "james"]
    
    def get_students_titlecase():
        
        students_titlecase = []
        
        for student in students:
            
            students_titlecase.append(student.title())
            
        return students_titlecase
    
    students_titlecase_names = get_students_titlecase()
    
    print(students_titlecase_names)
    
get_students()