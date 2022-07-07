# pooch.py - Continued from dog.py to call individual functions from a module

# Make individual "dog" module functions available
from dog import bark, lick, nap

#Next call each function without supplying an argument
bark()
lick()
nap()

#Now call each function again and pass an argument value to each then save the file
bark('Pooch')
lick('Pooch')
nap('Pooch')

#Continued in next program as fido.py

