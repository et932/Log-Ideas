from django.db import models
from django.utils import timezone


class LogIdeas(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=60)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message"""
        date = timezone.localtime(self.log_date)
        return f"'{self.name}''{self.description}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

