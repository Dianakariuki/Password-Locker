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