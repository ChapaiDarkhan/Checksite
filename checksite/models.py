from django.db import models
import requests


class Site(models.Model):
    url = models.URLField(unique=True)
    status_code = models.IntegerField(null=True, blank=True)
    # Using TextField here because sqlite3 not supporting JSONField
    extra_data = models.TextField(null=True, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

    def __str__(self):
        return self.url

    def check_status(self):
        response = requests.get(self.url)
        self.status_code = response.status_code
        self.extra_data = response.json()
        self.save()
