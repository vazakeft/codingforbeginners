# return.py - Demonstrate return statements

# Initialize a new variable with user input of an integer value for manipulation
num = input('Enter An Integer:')

#Add a function definition that accepts a single argument value to be passed from the caller
def square(num):

#Insert into the function block an indented statement to validate the passed argument value as an integer or halt further execution of the function's statements
    if not num.isdigit():
            return 'Invalid Entry'

# Add this indented statement to cast the passed argument value as an int data type then return the sum of squaring that value to the caller
    num = int(num)
    return num*num

#Finally add a statement to output a string and the returned value from the function call
print(num, 'Squared ls:', square(num))

#Save & Run
