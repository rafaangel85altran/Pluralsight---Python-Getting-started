'''
Created on 18 may. 2018

@author: win7
'''

if __name__ == '__main__':
    
    student = {
        #keys           #Values
        "name" :        "Mark",         #this key value pair is name = Mark
        "student_id" :  15163,
        "feedback" :    None
    }
    
    
    #Added the last name sepparately
    student ["Last name"] = "Kowalsky"
    
    try:
        last_name = student["Last name"]
        numbered_last_name = 3 + last_name
    except KeyError:
        print("Error finding last name")
    except TypeError as error:
        print("Error using incorrect data type")
        print(error)
    """except Exception:
        print("Unknow error") #When any exception non defined is trigged it will be shown this one
                              #not a good idea to use only this exception"""
    
    pass