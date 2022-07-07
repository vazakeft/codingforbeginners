# while.py - Demonstrate while loops, or known in the book, "Looping Conditions"

#Start by initializing a counter variable and define an outer loop using the counter variable
i = 1
while i < 4 :

#Next add the indented statement, to display the counter's values and increment for each pass/iteration
    print('Outer Loop Iteration:',i)
    i +=1

#Now, still indented, initialize a second "counter" variable and define inner loop using this expr.
    j = 1
    while j < 4:

#finally, add a further indented statement to display this counters value and increment
        print('\tInner Loop Iteration')
        j+=1