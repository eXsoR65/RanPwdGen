#!/bin/python3

# import the necessary modules!
import random
import string

# banner
print(
    '''
------------------------------------------------------------------------------
   ______                 ______              _   ______               
  (_____ \               (_____ \            | | / _____)              
   _____) )  ____  ____   _____) ) _ _ _   _ | || /  ___   ____  ____  
  (_____ (  / _  ||  _ \ |  ____/ | | | | / || || | (___) / _  )|  _ \ 
        | |( ( | || | | || |      | | | |( (_| || \____/|( (/ / | | | |
        |_| \_||_||_| |_||_|       \____| \____| \_____/  \____)|_| |_| - v2
-------------------------------------------------------------------------------
https://github.com/eXsoR65/RanPwdGen                                                                  
'''
)
# input the length of password
print('(Maximum possible character length: 94)')
length = int(
    input('Enter the length of password: '))

# genarate a password
genarate = string.ascii_letters + string.digits + string.punctuation

# create the password
passwd = "".join(random.sample(genarate, length))

# prints the password
print()  # space
print('Password: ', passwd)
print()  # space
