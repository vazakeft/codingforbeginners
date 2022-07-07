# continue.py (continuation of nest.py AND-> break.py) - Demonstrate Break Statements and nested loops

#Create a loop that iterates 3 times
for i in range(1,4):
    
#Next add an indented statement, that also creates a nested loop that also iterates 3 times
    for j in range(1,4):

#Now, further indent the inner loop to display counter numbers
        print('Running i=', i, 'j=', j)
        
#CONTINUED AS break.py
#Insert a break statement at the start of the inner loop to break off from that loop
        if i==2 and j==1:
            print('Breaks inner loop at i=2 j=1')
            break

#CONTINUED AS continue.py
        if i==1 and j==1:
            print('Continues inner loop at i=1 j=1')
            continue