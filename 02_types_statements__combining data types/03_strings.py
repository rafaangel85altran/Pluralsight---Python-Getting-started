'''
Created on 18 may. 2018

@author: win7
'''

if __name__ == '__main__':
    
    #Strings can be defined on any of this ways
        #'Hello world' == "Hello world" == """Hello world"""
    
    #Capitalize will make the first letter uppercase
    print("hello".capitalize())
    
    #Replace will replace a letter by other
    print("hello".replace("e", "a"))
    
    #isalpha will print true is characters are alphabetic
    print("hello2".isalpha())
    
    #isdigit will return true is characters are numeric
    print("123a".isdigit() == True)      #usefull when converting to string
    
    #slip is also usefull when comes to slip strings
    print("some,csv,values".split(","))
    
    #Another interesting function is format 
        #(Python is zero based)
    name = "PythonBo"
    machine = "HAL"
    print("Nice to meet you {0}, I´m {1}".format(name,machine))
    
    #Anoter way to do that
    print(f"Nice to meet you {name}, my name is {machine}")
    
    pass