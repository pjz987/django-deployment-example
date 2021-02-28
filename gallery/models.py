from django.db import models

class Photo(models.Model):

  image = models.ImageField(upload_to='images/')
  title = models.CharField(max_length=128)
  description = models.TextField()

  def __str__(self):
    return self.title