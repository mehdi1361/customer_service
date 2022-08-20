from django.core.management.base import BaseCommand, CommandError
from service.client.rayan.broker_customer import customer_list
from customer.models import Customer

class Command(BaseCommand):
    help = 'read data from rayan'

    def handle(self, *args, **options):
        for item in customer_list().result:
            print(item)
