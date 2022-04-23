#!/usr/bin/env python3.8
from credentials import Password


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