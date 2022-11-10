from os import path
import os
import string    
import random
#Imported Modules


#Removing old nitro codes.
if path.exists("all_codes.txt"):
    os.remove('all_codes.txt')

#Defines variables.
all_codes = str()

#Asks for settings.
code_amount = int(input('How many nitro codes would you like to generate? (Please enter only numbers)\n'))
print('\nYour codes are being generated!')

#Generating Codes.
for x in range(code_amount):
    current_code = str(''.join(random.choices(string.ascii_letters + string.digits, k = 16)))
    all_codes += current_code + '\n'

code_file = open('all_codes.txt', 'w+')
code_file.write(all_codes)
code_file.close()