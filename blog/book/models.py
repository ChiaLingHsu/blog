from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    pubDate = models.DateField(auto_now_add=True)
    version = '1'
    price = '1000'
    
    def __str__(self):
        return self.title    
# Create your models here.


# Create your models here.
