'''
Created on 18 may. 2018

@author: win7
'''

if __name__ == '__main__':
    
    # Dictionaries allow me to store key value pairs of any data very easily
    # Anyone who used json in the past will be very familiar
    
    student = {
        #keys           #Values
        "name" :        "Mark",         #this key value pair is name = Mark
        "student_id" :  15163,
        "feedback" :    None
    }
    
    #We can create a list of dictionaries
    all_students = [
        {"name": "Mark", "student_id": 15163, "feedback": None},
        {"name": "Katarina", "student_id": 15543, "feedback": True},
        {"name": "Willy", "student_id": 15653, "feedback": False}
    ]
    
    print("Acces directly to one element in the dictionary, for example ---> " + student["name"])
    
    #Be sure you don´t try to access to unexixtent keys inside of a dictionary
        #print(student["Last_name"])
    
    #get can be used to get a key and, in case this key is not present it will get the second argument
        #if not, it will take the actual existent key 
    print(student.get("Last_name","Unknow"))
    
    #You can access to the keys
    print(student.keys())
    
    #As well as the values
    print(student.values())
    
    #Changing values and delete them is the same as the lists
    student["name"] = "James"
    del student["name"]
    print(student.keys())
    print(student.values())
    
    
    
    pass