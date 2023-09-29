from django.db import models

class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=15)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    accept_language = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']