# coding: utf-8
from datetime import datetime
from django.db import models
from .. import settings

class Picture(models.Model):
    time_of_upload = models.DateTimeField(editable = False, auto_now_add = True)
    gallery = models.ForeignKey('Gallery', verbose_name = "Galleri")
    is_published = models.BooleanField(editable = True, verbose_name = "Publish", default = False)

    def pic_upload_to(instance, filename):
        return "gallery/" + str(instance.gallery.pk) + "/" + filename
    pic_file = models.ImageField(upload_to = pic_upload_to, verbose_name="Billede")
    def get_absolute_url(self):
        return settings.MEDIA_URL + unicode(self.pic_file)
    
class Gallery(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Titel")
    time_of_creation = models.DateTimeField(editable = False, auto_now_add = True)
    def __unicode__(self):
        return '[Galleri '+self.title+']'
    
    
