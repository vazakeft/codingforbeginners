# raise.py - demonstrate try, except, and finally statements

#Multiple exceptions can be handled by specifying their type as a comma-separate....
#...list in parentheses within the except block:

#initialize a variable with an integer value
day=32

#Add a try statement block that tests the variable value then specifies and exception and custom message
try:
        if day > 31:
                raise ValueError('Invalid Day Number')
        #More statesments to execute get added here

#Now add an except statement block to display an error message when ValueError occurs
except ValueError as msg:
        print('The program found an', msg)

#Finally, add a finally statement block to display an error message when a ValueError occurs
finally:
        print('But Today is beautiful anyways')
        