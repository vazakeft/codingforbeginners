# copy.py - Demonstrate a basic sorting algorithm

#Declare a function to receive a list reference as input and return a sorted copy as output
def copy_sort(array) :
    copy = array[ : ]
    sorted_copy=[]
 
 #Add the indented algorithm sequence to insert the copied element values into the empty list in order
    while len(copy) > 0:
        minimum = 0
        for element in range(0, len(copy)) :
            if copy[element]<copy[minimum] :
                minimum=element
        print('\tRemoving value', copy[minimum], 'from', copy)
        sorted_copy.append(copy.pop(minimum))
    
    #Send through return sorted_copy
    return sorted_copy


# Now add statements to create and display an unsorted list
array1 = [5, 3, 1, 2, 6, 4]
print('Copy Sort...\nArray:', array1)

#Add the statements to display the unsorted list and its sorted copy then save and run the program - to see the original list remains intact in unsorted order
print('Copy:', copy_sort(array1))
print('Array:', array1)


