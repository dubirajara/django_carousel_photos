from django.db import models
from django.db.models.fields.files import ImageFieldFile, FileField


class Photo(models.Model):
    title = models.CharField(max_length=60, default='', blank=True)
    description = models.TextField(max_length=200, default='', blank=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(width_field="width", height_field="height")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def get_pic(self):
        if self.image:
            return self.image
        return ImageFieldFile(instance=None, field=FileField(),
                              name='pictures/default.jpg')

    class Meta:
        ordering = ["timestamp"]
        verbose_name = 'Photo'

