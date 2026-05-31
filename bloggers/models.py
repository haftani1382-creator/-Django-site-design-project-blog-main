from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

class Blogger(models.Model):
    user = models.OneToOneField(User , on_delete= models.DO_NOTHING , default=0)
    name = models.CharField(max_length=200) 
    photo = models.ImageField(upload_to='photos/bloggers/%Y/%m/%d/')
    birth_date = models.DateField(default=datetime.now, blank=True) 
    register_date = models.DateField(default=datetime.now, blank=True) 
    posts_count = models.IntegerField(default=0)
    description = models.TextField()
    email = models.CharField(max_length=200) 
    phone = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name   #برای نمایش اسم بلاگر هنگام داینامیک کردن آن در بخش پست ها 
    

