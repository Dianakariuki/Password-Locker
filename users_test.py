import unittest
from users import User

class TestPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the Password class behaviours
    '''
def setUp(self):      
        
        
        self.new_users = User("Kariuki","Diana842")
       


def tearDown(self):
        '''
        Tear down method that does clean up after each test case has run
        '''
        User.users_list = []
        

def test__init(self):
        '''
        Test to check whether the credentials objects are instantiated correctly
        '''
        
        self.assertEqual(self.new_users.user_name,"Kariuki")
        self.assertEqual(self.new_users.user_passwrd,"Diana842")

def test_save_users(self):
        '''
        Test to check if the object is saved into the users list
        '''
        self.new_users.save_user()
        self.assertEqual(len(User.users_list),1)
        
        if __name__ == '__main__':
                unittest.main()