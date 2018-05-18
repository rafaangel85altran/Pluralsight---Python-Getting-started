'''
Created on 18 may. 2018

@author: win7
'''

if __name__ == '__main__':
    
    #Typical if else statement
    number = 1
    
    if number == 5:
        print("number is equal to 5")
    else:
        print("number is not equal to 5")
    
    #Truthy statement example
    value2 = None
    if value2:
        #truthy means that the variable has any value
        print("number is defined and truthy")
    else:
        print("number is not defined and is falsy")
    
    #Not equal example    
    if number != 4 :
        print("number is not equal to 4")
    
    #Another example of if is not ...
    if number is not 4:
        print("number is not equal to 4")
        
    #Multiple If conditions
    if number == 3 or value2 != 2:
        print("multiple if else")
    
    #Ternary if statements
    a = 1
    b = 2
    
    # For example if we want to display "bigger" if a > b else "smaller"
    print("bigger" if a > b else "smaller")
        
    
    

pass