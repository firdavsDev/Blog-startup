
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField 

from PIL import Image #rasm yuklash uchun kerak python -m pip install Pillow

#Profile model
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default="defaults.jpg",upload_to='profile_pics')

    def __str__(self) -> str:
        return f"{self.user.username}  Profile"


    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        
        #image size
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)