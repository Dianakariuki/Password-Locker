class User:
     '''
    class that creates instances of users
    '''
    
users_list = [] 

def __init__(self, user_name, user_passwrd):
        self.user_name = user_name
        self.user_passwrd = user_passwrd
def save_user(self):
        '''
        This method saves new object to users list
        '''
        User.users_list.append(self)