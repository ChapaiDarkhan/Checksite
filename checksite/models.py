from django.db import models
import requests


class Site(models.Model):
    url = models.URLField(unique=True)
    status_code = models.IntegerField()
    # Using TextField here because sqlite3 not supporting JSONField
    extra_data = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

    def __str__(self):
        return self.url

    def check_status(self):
        response = requests.get('https://api.github.com/user')
        self.status_code = response.status_code
