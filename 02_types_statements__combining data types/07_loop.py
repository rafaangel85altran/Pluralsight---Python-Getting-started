'''
Created on 18 may. 2018

@author: win7
'''

student_names = ["Johny", "Willy", "Mellony", "Pewee"]

if __name__ == '__main__':

    # For every name in student_names list, by default starts from the beginning and increment in 1
    for name in student_names:
        print("Student name is {0}".format(name))
    
    # Another way to do that
    x = 0
    for index in range(10):
        x += 10
        print("The value of X is {0}".format(x))
    
    # Range takes any value and convert it into a list
    print(range(10))        #from 0 to 9
    
    # Taking control of both the initial index and the last index value
    x = 0
    for index in range(5,10):                   # From 5 to 9, a total of 5 times
        x += 10
        print("The value of X is {0}".format(x))
    
    # Finally, if we want to set the first index, the last index and the increment
    x = 0
    for index in range(5,12,2):                 # From 5 to 11 in increments of 2
        x += 10
        print("The value of X is {0}".format(x))
    
    # But if I wnt to exit the loop before all I need to do is to set a break
    x = 0
    for index in range(5,12,2):                 # From 5 to 11 in increments of 2
        x += 10
        print("The value of X is {0}".format(x))
        if x == 20:
            print("Exit the loop before the last iteration")
            break
    pass