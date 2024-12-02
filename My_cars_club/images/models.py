from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.html import mark_safe


class Car(models.Model):
    cars = models.CharField(max_length=100, help_text='Give me religions of cars')
    speed = models.IntegerField(blank=False, verbose_name="speed", )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.DecimalField(max_digits=4, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    image_car = models.ImageField(upload_to='cars')
    history = HistoricalRecords()

    def __str__(self):
        return self.cars

    @property
    def thumbnail_preview(self):
        if self.image_car:
            return mark_safe('<img src="{}" width="310" height="160" />'.format(self.image_car.url))
        return ""


class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title



