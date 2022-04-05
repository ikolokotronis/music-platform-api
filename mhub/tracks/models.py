from django.db import models
from django.conf import settings


def upload_location(instance, filename, **kwargs):
    """
    Location for the audio file
    """
    file_path = f'tracks/{instance.id}/audio/{filename}'
    return file_path


def img_upload_location(instance, filename, **kwargs):
    """
    Location for the image file
    """
    file_path = f'tracks/{instance.id}/img/{filename}'
    return file_path


class Track(models.Model):
    """
    Track model
    """
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    audio_file = models.FileField(upload_to=upload_location)
    img_file = models.FileField(upload_to=img_upload_location, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Override save method to get the pk of the track instance
        :param args:
        :param kwargs:
        :return:
        """
        if self.pk is None:
            saved_audio_file = self.audio_file
            saved_img_file = self.img_file
            self.audio_file = None
            self.img_file = None
            super(Track, self).save(*args, **kwargs)
            self.audio_file = saved_audio_file
            self.img_file = saved_img_file

        super(Track, self).save(*args, **kwargs)
