from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfileManager(BaseUserManager):
    '''Manager for user profiles'''

    def create_user(self, email, name, password=None):
        '''Create a new user profile'''
        if not email:
            raise ValueError('The user needs a valid email')
        
        email = self.normalze_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''Database model for the user in the system'''

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self) -> str:
        return self.email
    


    from rest_framework.views import APIView
    from rest_framework.response import Response


    class HelloApiView(APIView):
        """Test API View"""

        def get(self, request, format=None):
            """Returns a list of APIView features"""

            an_apiview = [
                'User http methods as function (get, post, patch, put, delete)',
                'Is similar to tradional Django view',
                'Gives you the most control over your API logic',
                'Is mapped manually to URL´s'
            ]

            return Response({'asd': 'Hello World!', 'an_apiview': an_apiview})