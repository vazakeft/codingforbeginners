# nest.py - Demonstrate Break Statements and nested loops

#Create a loop that iterates 3 times
for i in range(1,4):
    
#Next add an indented statement, that also creates a nested loop that also iterates 3 times
    for j in range(1,4):

#Now, further indent the inner loop to display counter numbers
        print('Running i=', i, 'j=', j)

        #Continue to break.py!!!