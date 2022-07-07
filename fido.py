# fido.py - Continued from first dog.py, then pooch.py to demonstrate importing individual functions from the greatest module up the tree, dog.py

#Make all "dog" modules available
from dog import *

#Request a user entry to overwrite the default parameter
pet = input('Enter a pet name:')

#Finally, call each function passing the user-defined value as the argument
bark(pet)
lick(pet)
nap(pet)

