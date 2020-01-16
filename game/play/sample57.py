# sample57.py

# To test relative path importing.

print('- __name__:', __name__)
print('- __package__:', __package__)

import os
print('- os.getcwd():', os.getcwd())

from ..sound import echo
print(echo)