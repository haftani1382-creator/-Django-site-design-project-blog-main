from django.db import models
from datetime import datetime 
from bloggers.models import Blogger

class Post(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.DO_NOTHING) 
    title = models.CharField(max_length=200)
    text = models.TextField() 
    comments_count = models.IntegerField(default=0)  
    likes_count = models.IntegerField(default=0)     
    post_date = models.DateTimeField(default=datetime.now, blank=True) 
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/') 
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self) -> str:
        return self.title

