# dog.py - Demonstrate individually imported functions from modules. dog.py is the base module and the other programs pooch.py and fido.py will import off of this

# Start a new module by defining a function that supplies a default string value to its parameter
def bark(pet = 'A Dog'):
        print(pet, 'Says WOOF!')

#Next, add two more function definitions that also supply default string values to their parameters.
def lick(pet='A dog'):
    print(pet,'Says WOOF!')

#Next, add two more function definitions that also supply default string values to their parameters
def lick(pet = 'A Dog'):
        print(pet, 'Drinks water')

def nap(pet = 'A Dog'):
        print(pet, 'Sleeps in the sun')

#Saved as dog.py so the module is named dog. Next called by pooch.py
