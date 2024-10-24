from django.db import models

# Create your models here.

class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
