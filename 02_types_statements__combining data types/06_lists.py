'''
Created on 18 may. 2018

@author: win7
'''

if __name__ == '__main__':
    
    #To define a list you first need to declare the name and then brackets
    
    student_names_empty = []                        #This is an empty python list
    
    student_names = ["Johny", "Willy", "Mellony"]   #This is an already filled list
    
    print(student_names[2])                         #You can access any element like vectors
    print(student_names[-3])                        #Acces can be from 0 to n or from -n to 0
    
    # If we need to add new elements to the list we cannot just do the following
        #student_names[3] = "Hommer"
    student_names.append("Hommer")
    
    print(student_names[3])
    
    #If we want to search any element in a list we can just type the following
    
    if "Willy" in student_names:
        print("Willy is still in student_names")
    else:
        print("No, is not there")
    
    print(len(student_names))                       #prints the total number of elements in a list
    
    #although you can add different data types inside the same list is best to avoid that to 
    #minimize possible bugs
    
    student_names.append(3.14159)
    
    print(student_names[4])
    
    #if we want to delete some element in a list we just use the del element
    del student_names[4]
    print(student_names)
    
    #list slicing, ignore temporary some elemts of the list
    print(student_names[1:])                        #ingnores the first element
    print(student_names[2:])                        #ingnores the first and second element
    print(student_names[1:-1])                      #ignores the first and the last element
    
    pass