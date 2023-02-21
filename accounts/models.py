from django.db import models

# Create your models here.
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/
    return 'user_{0}/{1}'.format('simpo/users/', filename)

class User(User):
    middle_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )
    phone_number= models.IntegerField()
    gender = models.CharField(
        max_length=10, 
        choices = (
            ('male', 'Male'),
            ('female', 'Female'),
            ),
        )
    profile_picture= models.FileField(upload_to=user_directory_path)
    
    