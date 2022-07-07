# param.py - See the function display the arguement values or parameter values

#Define a function with three parameters that will print out passed-in argument values
def echo(user, lang, sys):
        print('User:', user, 'Language:', lang, 'Platform:', sys)

#Call the function passing string argument values to the function parameters in the order they appear
echo('Mike', 'Python', 'Windows')

#Call the function passing string arguments to the function parameters by specifying the parameter names
echo(lang='Python', sys='Mac OS', user='Anne')

#Define another function with two parameters having default values that will print out parameter values
def mirror(user='Carole', lang='Python'):
        print('\nUser:', user, 'Language:', lang)

#Add statements to call the second function both using and overriding default values
mirror()
mirror(lang='Java')
mirror(user='Danny')
mirror('Susan', 'C++')

