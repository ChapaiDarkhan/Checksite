import logging
import re
import socket
from json import JSONDecodeError

import requests
from django.db import models
from django.utils import timezone
from requests import RequestException

logger = logging.getLogger(__name__)


class Site(models.Model):
    url = models.URLField(unique=True)
    status_code = models.IntegerField(null=True, blank=True)
    ip_address = models.CharField(null=True, blank=True, max_length=50)
    # Using TextField here because sqlite3 not supporting JSONField
    extra_data = models.TextField(null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

    def __str__(self):
        return self.url

    def check_status(self) -> None:
        try:
            url = self.url
            if not re.search('(?:http|https)://', url):
                url = 'http://{}'.format(url)
                response = requests.get(url)
                self.status_code = response.status_code
                self.extra_data = f'{response.headers}/n{response.encoding}'
                self.save()
        except RequestException as e:
            logger.error(f'For site.url {e}')
        except JSONDecodeError as e:
            logger.error(f'For site.url {e}')
        try:
            self.ip_address = socket.gethostbyname(self.url)
            self.save()
        except socket.error as e:
            print("Error:", self.url)
            logger.error(f'For site.url {e}')
