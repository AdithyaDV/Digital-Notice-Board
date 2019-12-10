from django.db import models

# Create your models here.
class Text(models.Model):

    screenNo = models.IntegerField(choices=((1, ("Screen 1")),
                                        (2, ("Screen 2"))),
                                   default=0
                                   )
    user = models.CharField(max_length=20, default='NULL')
    time = models.DateTimeField()
    text = models.CharField(max_length=100, default='NULL')
    endtime = models.DateTimeField(default='NULL')
