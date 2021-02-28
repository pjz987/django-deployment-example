from django.shortcuts import render
from django.http import HttpResponse

from .models import Photo
from .forms import PhotoForm

def index(request):
  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    print(form)
    if form.is_valid():
      form.save()
  else:
    form = PhotoForm()
  gallery = Photo.objects.all()
  context = {
    'gallery': gallery,
    'form': form,
  }
  return render(request, 'gallery/index.html', context)