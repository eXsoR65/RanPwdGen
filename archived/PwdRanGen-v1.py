#!/bin/python3

import random

print('''
#   ______                 ______              _   ______               
#  (_____ \               (_____ \            | | / _____)              
#   _____) )  ____  ____   _____) ) _ _ _   _ | || /  ___   ____  ____  
#  (_____ (  / _  ||  _ \ |  ____/ | | | | / || || | (___) / _  )|  _ \ 
#        | |( ( | || | | || |      | | | |( (_| || \____/|( (/ / | | | |
#        |_| \_||_||_| |_||_|       \____| \____| \_____/  \____)|_| |_| - v1
# https://github.com/eXsoR65/RanPwdGen                                                                  
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]:"'

number = input('Number of passwords?')
number = int(number)

length = input('Password length?')
length = int(length)

print('\nGenerated Passwords:')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
print('--End of password list--')
