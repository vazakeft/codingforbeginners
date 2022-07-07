# tiger.py - continuation from cat.py to later kitty.py to demo importing functions

# Start by importing cat.py
import cat

#Request a name to overwrite the default parameter value
pet = input('Enter a pet name:')

# Call each function passing the user-defined value as the argument
cat.purr(pet)
cat.lick(pet)
cat.nap(pet)

#Save and run tiger.py

