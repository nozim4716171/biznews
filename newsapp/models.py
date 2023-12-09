from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Kategoriya(models.Model):
    nomi = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nomi


class yangiliklar(models.Model):
    
    class Status(models.TextChoices):
        yuklash = "S","Successfully"
        qoralama = "F","Fail"
        
    nomi = models.CharField(max_length=255)
    slug = models.SlugField()
    matn = models.TextField()
    yaratilgan_vaqti = models.DateTimeField(auto_now_add=True)
    yuklangan_vaqti = models.DateTimeField(default=timezone.now)
    yangilash_vaqti = models.DateTimeField(auto_now=True)
    rasm = models.ImageField(upload_to='news/rasm')
    kategoriya = models.ForeignKey(Kategoriya, on_delete=models.CASCADE)
    status = models.CharField(max_length=1,
                            choices=Status.choices,
                            default=Status.qoralama)
    def __str__(self):
        return self.nomi
    
    def get_absolute_url(self):
        return reverse('newsdetail', args=[str(self.slug)])

class Contact(models.Model):
    ism = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Comment(models.Model):
    news = models.ForeignKey(yangiliklar, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    