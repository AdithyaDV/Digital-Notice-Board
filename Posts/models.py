from django.db import models

# Create your models here.
class Post(models.Model):
    screenNo = models.IntegerField(choices=((1, ("Screen 1")),
                                        (2, ("Screen 2"))),
                                   default=0
                                   )
    user = models.CharField(max_length=20, default='NULL')
    image = models.ImageField(upload_to='images/', default='NULL')
    time = models.DateTimeField()
