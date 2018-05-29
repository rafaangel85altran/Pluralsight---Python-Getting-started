'''
Created on 22 may. 2018

A function is a block of organice and reusable code which is used to perform a certain action

@author: win7
'''

"""
HOMEWORK: Ask the user if we wants to add a new student to the list, if yes then enter a new name 
and id and sak again until the user donesn´t want to, then the program will print the entire list
of students entered so far and check if some student_id is duplicated
"""

students = []

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

    
def add_student(name, student_id=332):
    student = {"name" : name, "student_id" : student_id}      
    students.append(student)

"""
ADD function to store the data in a txt file
"""

def save_file(student):
    try:
        f = open("students.txt", "a")       # Append or create a new file
        for x in student:
            f.write(x + "\n")               # 
        f.close()
    except TypeError as error:
        print("File could not be saved")
        print(error)
        
def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("File could not be read")
    
student_list = get_students_titlecase()


print("##### Welcome to the add_students program #####")    
response = input("Do you want to add a user to your list? (Y/N)")

while response == "Y":
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    add_student(student_name, student_id)
    response = input("Do you still want to add more students? (Y/N)")

    
if students_id_check() == True:
    print("Carefull, at least one student id is duplitaced, please check it out")
else:
    save_file(students)
    
print_students_dict_org()
read_file()



    

