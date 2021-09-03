from typing import FrozenSet
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
from django.urls import reverse

from django.utils import timezone
from django.contrib.auth.models import User #bazadagi ruyhatdan utkanlar uchun

#POST MODELIMIZNI YARIB OLAMIZ 
# python manage.py sqlmigrate blog 0001 ---- bu sql holatda kurish migrate bulgan malumotni
# python manage.py shell ----- terminaldan boshqarish

class Post(models.Model):
    image = models.ImageField(null=False, blank=False)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #hozirgi vaqtni olamiz
    author = models.ForeignKey('auth.User',related_name='posts',on_delete=models.CASCADE) #agar ruyhatdan utgan insoni akkounti uchirilsa uning postlari ham uchib ketadi
    #like
    likes = models.ManyToManyField(User,related_name='blog_posts')
    #likes soni
    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


