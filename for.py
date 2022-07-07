# for.py - Demonstrate Python Looping with for statements

#Create a regular list, a fixed tuple list, and an associative dictionary list
chars = ['A', 'B', 'C']
fruit = ('Apple', 'Banana', 'Cherry')
info = {'name' : 'Mike', 'ref' : 'Python', 'sys' : 'Win' }

#Add statements to display all list element values
print('Elements: \t', end='')
for item in chars:
        print(item, end='')

#Add statements to display all list element values and their relative index number
print('\nEnumerated:\t', end='')
for item in enumerate(chars):
        print(item,end='')

#Next, add statements to display and list all the tuple elements
print('\nZipped: \t', end ='')
for item in zip(chars,fruit):
        print(item,end='')

#Add statements to display dictionary key names and associated element values
print('\nPaired:')
for key, value in info.items():
        print(key, '=', value)