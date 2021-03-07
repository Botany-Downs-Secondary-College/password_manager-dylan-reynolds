#Dylan Reynolds
#Simple python programs to save passwords

#Declares variables
menu = 0
name = ' '
age = 0
account = ['login','123']
username = ' '
password = ' '
password_list = []

#imports
import os
import time
import sys


#Declares functions to keep Console tidy
def delete():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def clear():
    os.system('cls')

def tiny():
    time.sleep(1)

def small():
    time.sleep(2)

def medium():
    time.sleep(5)

#Login Menu functions
def login():
    tiny()
    clear()
    print('''
  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
|       Welcome exiting member! Input your credentials here.       |
|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |
''')
    username = input('  What is your username?: ')
    username.strip()
    password = input('  What is your password?: ')
    password.strip()
    if username in account and password in account:
        print('\n Login Successful! You will be redirected shortly.')

def signup():
    tiny()
    clear()
    print('''
  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
|         Welcome New member! Create your credentials here.        |
|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |''')
    username = input('  Create your username: ')
    username.strip()
    while True: 
        password = input('  Create your password (minimum 8 characters): ')
        password.strip()
        account.append([username, password])
        if len(password) < 8:
            delete()
            print('  Your password is not 8 characters please try again')
            medium()
            delete()
        elif len(password) >= 8:
            print('  Account Successfully Created!')
            break
   
def leave():
    small()
    clear()
    print('''
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
|                                                       |
|                   goodday to you!                     |
| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |    
''')
    exit()

#Clears console before hand
clear()

#Introduction to the program.
print('''\
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
|_       __          __                                 |
| |     / /  ___    / /  _____  ____    ____ ___   ___  |
| | /| / /  / _ \  / /  / ___/ / __ \  / __ `__ \ / _ \ |
| |/ |/ /  /  __/ / /  / /__  / /_/ / / / / / / //  __/ |
|__/|__/   \___/ /_/   \___/  \____/ /_/ /_/ /_/ \___/  |
| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |           
| To the 2020 offical password manager application mana-|
|-ged by yours truely! copyright - 2020 all rights reser|
| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |                                              
''')

medium()
clear()

print('''
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
|                                                       |
| This Program is not to be used by people under the age|
| of 13 years due to legal requirements!                |
| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |
''')

medium()
clear()

#Asks the user their age and if its under 13 declines them
name = input('''
  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
| Before the program can continue you must validate your age here! |
|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |
    What is your name?: ''')
name.strip()

age = int(input('    What is your age?: '))

small()
clear()

if age < 13:
    print('''
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
|                                                       |
|         you are too young to use this program         |
|                   goodday to you!                     |
| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |

''')

#Routine for the Login Page
while True: 
    menu = int(input('''
  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
|  Welcome to the login page! Press 1 to make login to an existing |
|  account, press 2 to create a new account and press 3 to exit!   |  
|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |
    : '''))
    if menu == 1:
        login()
        break
    elif menu == 2:
        signup()
        break
    elif menu == 3:
        leave()
    else:
        print('    That was an invalid response please input a number from 1 to 3!')
        small()
        clear()
        
#Routine for Password Manager
    