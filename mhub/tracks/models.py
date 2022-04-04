from django.db import models
from django.conf import settings


def upload_location(instance, filename):
    """
    Location for the audio file
    """
    file_path = 'tracks/%s/%s' % (instance.user.username, filename)
    return file_path


class Track(models.Model):
    """
    Track model
    """
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    audio_file = models.FileField(upload_to=upload_location)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
