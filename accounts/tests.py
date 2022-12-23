from django.test import TestCase
from django.urls import resolve

# Create your tests here.
from . import views
from django.contrib.auth.models import User

# Create your tests here.

class UsersTest(TestCase):
    class MockRequest:
                POST = {}
    def test_unprivileged_user(self):
        pass

    def test_sign_up(self):
        found = resolve('/accounts/signup').func
        self.assertEqual(found, views.signup)
        users = {
            'normal_user':{
                'username' : 'John',
                'email' : 'John@doe.com',
                'password' : 'unsafe',
                'pass' : True
                },
            'incorrect_email_user':{
                'username' : 'Jane',
                'email' : 'JaneDoe.com',
                'password' : 'unsafe',
                'pass' : False
            },
            'same_email_as_normal_user':{
                'username' : 'Jane',
                'email' : 'John@doe.com',
                'password' : 'unsafe',
                'pass' : False
            },
            'missing_password':{
                'username' : 'Qwerty',
                'email' : 'Qwerty@doe.com',
                #'password' : 'unsafe',
                'pass' : False
            },
            
           
        }
        
        request = UsersTest.MockRequest()
        for user in users:
            request.POST = users[user]
            try:
                views.signup(request=request)
            except Exception:
                self.fail(msg=f'Testing {user}')
            user_exists = len(User.objects.filter(username=request.POST['username'],email=request.POST['email'])) == 1
            self.assertEqual(request.POST['pass'],user_exists, msg=f'Testing {user}')


    def test_login(self):
        users = {
            'normal_user':{
                'username' : 'John',
                'email' : 'John@doe.com',
                'password' : 'unsafe',
                'pass' : True
                },
            'incorrect_email_user':{
                'username' : 'Jane',
                'email' : 'JaneDoe.com',
                'password' : 'unsafe',
                'pass' : False
            },
            'missing_password':{
                'username' : 'Qwerty',
                'email' : 'Qwerty@doe.com',
                #'password' : 'unsafe',
                'pass' : False
            },
        }
        
            