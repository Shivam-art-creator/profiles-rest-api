from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        """set_password() function used to encrypt password by default"""
        user.set_password(password)
        user.save(using=self.db)

        return user


    def create_superuser(self,email,name,password):
        """create and save a new superuser with given details"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Rerieve short name of user"""
        return self.name

    def __str__(self):
        """Return String representation of our user"""
        return self.email



class ProfileFeedItem(models.Model):
    """Profile status update"""

    # Define a ForeignKey field to link each feed item to a user profile
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the user model specified in settings
        on_delete = models.CASCADE  # Cascade delete if user profile is deleted
    )

    # Define a CharField to store the text of the status update
    status_text = models.CharField(max_length=255)

    # Define a DateTimeField to store the creation date of the feed item
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text









