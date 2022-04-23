#!/usr/bin/env python3.8
from credentials import Password


def create_credential(sname, fname, lname, password):
    '''
    Function to create a new user credentials
    '''
    new_credential = Password(sname, fname, lname,password)
    return new_credential