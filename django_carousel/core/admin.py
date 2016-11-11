from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoCarouselAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]

    class Meta:
        model = Photo
