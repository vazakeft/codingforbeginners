# try.py - Demonstrate try statements

#Initialize variable with a string title
title='Coding for Beginners in Easy Steps'

#Add a try statement that attempts to display the variable value - but is incorrectly specified "titel"
try:
        print(titel)

#Add an except statement block to display the error message when a NameError occurs
except NameError as msg:
    print(msg)
