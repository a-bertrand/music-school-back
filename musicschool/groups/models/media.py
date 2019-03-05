from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
# TODO READ TO ADD Guitar pro Lecteur 
# https://ourcodeworld.com/articles/read/399/how-to-display-guitar-pro-tabs-in-the-browser-with-javascript-using-alphatab
class Media(models.Model):
    name        = models.CharField(max_length=30)
    video       = models.FileField(upload_to='videos',  null=True, blank=True)
    image       = models.FileField(upload_to='images',  null=True, blank=True)
    pdf         = models.FileField(upload_to='pdf',     null=True, blank=True)
    audio       = models.FileField(upload_to='audio',   null=True, blank=True)
    guitarpro   = models.FileField(upload_to='gp',      null=True, blank=True)
    youtubeurl  = models.CharField(max_length=50,       null=True, blank=True)
    text 	    = models.TextField(max_length=200,     null=True, blank=True)

    def __str__(self):
        return self.name

    def image_url(self):
        return ("/musicschool/media/%s" % (self.image))
    
    def get_youtube_url_clean(self):
        base_youtube_url = "https://www.youtube.com/embed/"
        return f"{base_youtube_url}{self.youtubeurl}"
        
