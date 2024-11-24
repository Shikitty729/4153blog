from django.db import models

# Create your models here.
# todo: enhance this model later

class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_object_name = models.CharField(max_length=100, null=True)
