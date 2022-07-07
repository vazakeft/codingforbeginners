# if.py - Doing if/elif/else statements for the first time in Python

#Initialize a variable with user input of an integer value
num=int(input('Please Enter A number:'))

#Test the variable and display an appropriate response
if num>5:
    print('number exceeds 5')
elif num<5:
    print('number is less than 5')
else:
    print('number is 5')

#Now test the variable again using two expressions and display a response only upon success
if num > 7 and num < 9:
    print('Number is 8')
if num == 1 or num == 3:
    print('Number is 1 or 3')

#done
