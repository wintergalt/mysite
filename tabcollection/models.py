from django.db import models
import datetime

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.name
        

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist)
    year = models.IntegerField(null=True)
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    mp3_file = models.FileField(upload_to='mp3')
    
    def __unicode__(self):
        return '{0} - {1}'.format(self.title,self.artist)