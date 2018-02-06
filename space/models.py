from django.db import models
from django.utils import timezone


class Space(models.Model):
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    read = models.BooleanField()

    def publish(self):
        self.published_date = timezone.now()
        self.read = False
        self.save()

    def __str__(self):
        return self.text
