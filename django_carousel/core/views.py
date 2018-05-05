from django.shortcuts import render

from .models import Photo


def photo_carousel(request):
    queryset = Photo.objects.all()
    context = {
        "photos": queryset,
    }
    return render(request, 'bootstrap.html', context)
