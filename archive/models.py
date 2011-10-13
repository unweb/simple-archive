from django.db import models

# Create your models here.
from django.db import models
import datetime

class Event(models.Model):
    "A very basic model for Events"
    name = models.CharField('A name for the event', max_length=200)
    place = models.CharField('Location where the event takes place',
                             max_length=200)
    date = models.DateField('When the event takes place')

