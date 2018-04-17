from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(u'video url ',max_length=256 )
    content = models.TextField(u'content')
    phone = models.IntegerField(u'phone')
    address = models.CharField(u'address',max_length=256)

    def __unicode__(self):
        return self.title