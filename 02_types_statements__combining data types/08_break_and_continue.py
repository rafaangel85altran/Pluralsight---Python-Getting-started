'''
Created on 18 may. 2018

@author: win7
'''

if __name__ == '__main__':
   
    student_names = ["James", "Johny", "Willy", "Bort", "Mark", "Pitty"]
    
    # Break can be used to exit the loop in any moment
    for name in student_names:
        if name == "Mark":
            print("Found Mark!")
            break
        print("currently testing " + name)
    
    print("######################################################################")
    
    # Continue can be used to increment the loop in any case, to ignore certany elements
    for name in student_names:
        if name == "Bort":
            continue
            print("Now this code cannot be reached")
        print("currently testing " + name)
     
    pass