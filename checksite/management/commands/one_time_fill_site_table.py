import csv
from abc import ABC
from django.core.management import BaseCommand

from checksite.models import Site


class Command(BaseCommand, ABC):
    WEBSITES_TABLE = 'checksite/data/websites.csv'

    def handle(self, *args, **options):
        with open(self.WEBSITES_TABLE, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            count = 0
            for row in reader:
                url = row['url']
                is_site_exists = Site.objects.filter(url=url).exists()
                if not is_site_exists:
                    Site.objects.create(url=row['url'])
                    count += 1

                    if count % 100 == 0:
                        self.stdout.write(f'{count} sites was created')
            self.stdout.write(f'{count} sites was created')
