import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                new_phone = Phone(
                    id=phone['id'],
                    name=phone['name'],
                    image=phone['image'],
                    price=float(phone['price']),
                    release_date=phone['release_date'],
                    lte_exists=bool(phone['lte_exists'])
                )
                new_phone.save()
                self.stdout.write(self.style.SUCCESS(f'Phone "{new_phone.name}" imported successfully'))

