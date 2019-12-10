from django.db import models


# Create your models here.
class Video(models.Model):
    screenNo = models.IntegerField(choices=((1, ("Screen 1")),
                                            (2, ("Screen 2"))),
                                   default=0
                                   )
    user = models.CharField(max_length=20, default='NULL')
    file = models.FileField(upload_to='video/', default='NULL')
    durationInSeconds = models.IntegerField(default=60)
    time = models.DateTimeField()
    endtime = models.DateTimeField(default='NULL')

