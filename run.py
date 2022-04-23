#!/usr/bin/env python3.8
from credentials import Password
import sys
import random
import string
from users import User
from termcolor import colored, cprint
#from termcolor import colored, cprint

def create_credential(sname, fname, lname, password):
    '''
    Function to create a new user credentials
    '''
    new_credential = Password(sname, fname, lname,password)
    return new_credential


def save_credential(credential):
    '''
    Funtion to save the credential
    '''
    credential.save_credential()
    
def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()  
    
def find_credential(site_name):
    '''
    Function to find a credential
    '''
    return Password.find_by_account_name(site_name)


def check_existing_credentials(account_name):
    '''
    Function to check whether a credential exists
    '''
    return Password.credential_exist(account_name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Password.display_credentials()



def create_user(username, psswrd):
    '''
    Function to create a new user credentials
    '''
    new_user = User(username, psswrd)
    return new_user

def save_users(user):
    '''
    Funtion to save the credential
    '''
    user.save_users()
    
    
    #CAllING THE FUNCTIONS
    
def main():
    cprint("Hello, Welcome to Password Locker. What is your name?", "magenta")
    user_name = input("Name:")

    while True:
        print(f"Hello {user_name}, Please use these short codes to either login to your account or sign in.") 
        cprint("lg - log into your account", "magenta")
        cprint("ca - create an account", "magenta")
        s_code = input("Short Code:").lower()

        if s_code == 'ca':
            print("Enter username")
            fusername = input()

            print("Enter password")
            fpin = input()

            

            cprint("You have successfully created an account", "green")
            cprint("Please proceed to log in", "magenta")
            cprint('\n')

        
        
            print("Enter your username")
            username = input()
            

            print("Enter your password")
            pin = input()

            if username == fusername and pin == fpin:
                cprint("lOGIN SUCCESSFUL", "green")
                print('\n')
                pass
                while True:
                    cprint("Use these short codes: sc - Save existing credentials, cc - Create new credentials, dc - display credentials, fc - Find a credential, delete - delete credentials, ex-exit the account", "magenta")

                    short_code = input().lower()

                    if short_code == 'cc':
                        print("New Credentials")
                        print("-"*10)

                        print("Site Name...")
                        sname = input("Site Name: ")

                        print("First Name")
                        fname = input("")

                        print("Last Name....")
                        lname = input()

                        print("Would you like a generated password, type yes/no")
                        password = input().upper()
                        if password == 'YES':
                            print("How long would you like your password to be?")
                            password_length = int(input())
                            chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
                            my_pass = "".join(random.choice(chars) for i in range(password_length))
                       
                        elif password == 'NO':
                            print("Enter your preferred password")
                            my_pass = input()

                        else:
                            cprint("Unrecognised input", "yellow")

                        save_credential(create_credential(sname, fname, lname, my_pass)) #Create and save credentials
                        print('\n')
                        print('-'*30)
                        cprint(f"New Credential {fname} {lname} created", )
                        print('-'*30)
                        print('\n')

                    elif short_code == 'sc':
                        print("Save Existing credentials")
                        print("-"*10)

                        print("Site Name...")
                        sname = input()

                        print("First Name")
                        fname = input()

                        print("Last Name")
                        lname = input()

                        print("Password")
                        password = input()

                        
                    
                        save_credential(create_credential(sname, fname, lname, password)) #Create and save credentials
                        print('\n')
                        print(f"{sname} credentials saved")
                        print('\n')


                    elif short_code == 'dc':
                        if display_credentials():
                            cprint("Here is a list of all you credentials", "yellow")
                            print('\n')

                            for credential in display_credentials():
                                cprint(f"{credential.account_name}", "yellow")
                                print("-"*30)
                                print(f"Username: {credential.first_name} {credential.last_name}")
                                print(f"Password: {credential.user_password}")
                                print('\n')

                        else:
                            print('\n')
                            cprint("You don't seem to have any credentials saved yet", "red")
                            print('\n')

                    elif short_code == 'fc':
                        cprint("Please enter the site name you want to search for", "magenta")

                        search_site = input("Site Name: ")
                        if check_existing_credentials(search_site):
                            search_site = find_credential(search_site)
                            cprint(f"{search_site.first_name} {search_site.last_name}", "yellow")
                            print("-"*20)

                            cprint(f"Password.....{search_site.user_password}", "yellow")

                        else:
                            cprint("These credentials do not exist", "red")
                            print('\n')

                    elif short_code == 'delete':
                        cprint("Please enter the name name of the site you want to delete","magenta")
                        site_delete = input()
                        if check_existing_credentials(site_delete):
                            site_delete = find_credential(site_delete)
                            delete_credential(site_delete)

                            cprint("Credentials deleted successfully", "green")

                        else:
                            cprint("Credentials do not exist", "red")


                    elif short_code == "ex":
                        cprint("Bye.....", "yellow")
                        print('\n')
                        print('-'*20)
                        break
                    else:
                        cprint("I really didn't get that", "red")
            else:
                cprint("Invalid login details", "red")
                print('\n')

        elif s_code == 'lg':
            print("Please Enter your name")
            inputname = input()

            print("Enter Your Password")
            inputpass = input()

            cprint("The login details you entered do not seem to exist. Please create an account before you can login", "red")
            print('\n')
    

        

    




if __name__ == '__main__':
    
    main()