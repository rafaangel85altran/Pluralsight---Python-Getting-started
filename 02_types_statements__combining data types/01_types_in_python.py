'''
Created on 18 may. 2018

@author: win7
'''

if __name__ == '__main__':
    
    #There is no need to declare the data type once you declare a variable
    def add_numbers(a, b):
        print(a + b)
        
    print("This is the function being called with the correct datatype parameters")
    print(add_numbers(5, 11))
    
    #But be carefull not to use the incorrect data types
    #print("You can mess it up using the incorrect data types")
    #print(add_numbers(5, "somethin"))
    
        # In python the program compiles directlyand encounter the error, in C++ the compiler will
        # find a problem and prevent you from compiling
        
    #This other way to declare a fucntion tells the datatyoe of the arguments as well as the return
    def add_numbers_with_data_types(a: int, b: int) -> int:
        return a+b
    print("This is a function that adds ints with data type implicit")
    print(add_numbers_with_data_types(5, 11))
        
    
    pass