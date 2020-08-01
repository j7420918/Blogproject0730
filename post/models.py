from django.db import models


class Post (models.Model):
    title=models.CharField(max_length=200)
    body = models.TextField()
    image= models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] 







# Create your models here.
