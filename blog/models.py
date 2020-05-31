from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class short_urls(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.URLField("URL", unique=False)
    clickedDate = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)