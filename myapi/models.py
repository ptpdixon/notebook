from django.db import models
from django.utils import timezone

class Note(models.Model):
  title = models.CharField(max_length=60)
  subject = models.CharField(max_length=10, default='Junk')
#   subject = models.TextChoices('Subject', 'Physics Chemistry Biology')
  content = models.TextField()
  modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title