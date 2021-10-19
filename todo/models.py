from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Vazifa(models.Model):
    user = models.ForeignKey(User,related_name='todos',on_delete=models.CASCADE,blank=True,null=True)
    mavzu=models.CharField(max_length=200)
    tugadi=models.BooleanField(default=False)
    yaratish=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.mavzu