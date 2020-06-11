from django.db import models
from django.conf import settings
from django.utils import timezone
from . import voice_recogition

class Post(models.Model):
#    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
#    text = models.TextField()
#    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
#
    def publish(self):
        self.published_date = timezone.now()
        self.save()
#
    def __str__(self):
        return self.title

# Create your models here.

class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    #upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

#def exec_voice_recognition(request):
#    file = ...
#   result = voice_recogition.recognize(file)
#    ...