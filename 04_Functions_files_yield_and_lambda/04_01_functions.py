'''
Created on 22 may. 2018

A function is a block of organice and reusable code which is used to perform a certain action

@author: win7
'''
students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print (students_titlecase)
    
def add_student(name, student_id=332):
    student = {"name" : name, "student_id" : student_id}      
    students.append(student)       
    
student_list = get_students_titlecase()
    
add_student(name="Johny", student_id=15)
    
#If I try to do this
    #print(name)            #unresolved reference "name"
    
"""def add_student(name, student_id=332):   #By adding "=332" (value of number doesn´t matter)
    students.append(name, student_id)       # we´re declaring this argument 332 as optional
"""

"""
There is a type of function with a variable number of arguments like print(arg1, arg2, arg3, ..., argn)

def var_args(name, *args):
        print(name)
        print(args)
        
var_args("Mark", None, True, 483240932, "Loves Python")

"""

"""This is a veri flexible way to add a variable number of arguments to any function
def var_args(name, **kwargs):
        print(name)
        print(kwargs["description"], kwargs["feedback"], kwargs["pluralsight_subscriber"])
        
var_args("Mark", description="Loves Python", feedback=None, pluralsight_subscriber=True)
"""