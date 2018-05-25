'''
Created on 22 may. 2018

A function is a block of organice and reusable code which is used to perform a certain action

@author: win7
'''
students = [
        {'name': 'Rafa', 'student_id': '123'},
        {'name': 'Johny', 'student_id': '124'},
        {'name': 'Mahoney', 'student_id': '126'},
        {'name': 'Sleider', 'student_id': '126'},
        {'name': 'Makajohny', 'student_id': '128'}
    ]

def students_id_check():
    
    list_of_all_ids = []
    
    for id_number in range(len(students)):
        list_of_all_ids.append(students[id_number]["student_id"])
    
    if len(list_of_all_ids) != len(set(list_of_all_ids)):
        return True
    else:
        return False
    
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase


def print_students_dict_org():
    for x in students:
        print (x)  

"""
def print_students_titlecase():
    #students_titlecase = get_students_titlecase()
    print (students)
""" 
    
def add_student(name, student_id=332):
    student = {"name" : name, "student_id" : student_id}      
    students.append(student)
        
student_list = get_students_titlecase()

"""    DISABLED THE STUDENT ENTER INTERFACE FORTESTING PURPOSES
print("##### Welcome to the add_students program #####")    
response = input("Do you want to add a user to your list? (Y/N)")

while response == "Y":
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    add_student(student_name, student_id)
    response = input("Do you still want to add more students? (Y/N)")
"""   
    
if students_id_check() == True:
    print("Carefull, at least one student id is duplitaced, please check it out")

print_students_dict_org()


"""
HOMEWORK: Ask the user if we wants to add a new student to the list, if yes then enter a new name 
and id and sak again until the user donesn´t want to, then the program will print the entire list
of students entered so far 
"""


