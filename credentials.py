class Password :
    '''
    class that creates instances of users accounts credentials
    '''
    
credentials_list = []

def save_credential(self):
        '''
        Method to save a new object in the credential list
        '''
        Password.credentials_list.append(self)
        
        
        
def delete_credential(self):
        '''
        Method to delete a credential from the list
        '''
        Password.credentials_list.remove(self)