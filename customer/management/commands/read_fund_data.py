from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from service.client.rayan.broker_customer import fund_customer_list
from customer.models import Customer, CustomerFund, CustomerPhonePerson

class Command(BaseCommand):
    help = 'read fund data from rayan'

    def handle(self, *args, **options):
        for service in ("fund1", "fund2"):
            for item in fund_customer_list(service).result:
                with transaction.atomic():
                    customer, _ = Customer.objects.get_or_create(
                        normal_national_code=str(
                            item.national_identifier
                        ).replace("_", "").replace("-", "").strip(),
                        defaults={
                            "is_rayan_service": True
                        }
                    )

                    customer_fund, _ = CustomerFund.objects.get_or_create(
                        customer_service=customer,
                        fund_name=service,
                        defaults={
                            "customer_id": item.customer_id,
                            "referred_by": item.referred_by,
                            "account_number": item.account_number,
                            "personality": item.personality,
                            "fullname": item.customer_full_name,
                            "is_profit_issue": item.is_profit_issue,
                            "issuing_city": item.issuing_city,
                            "nationality": item.nationality,
                            "creation_date": item.creation_date,
                        }
                    )
                    for phone in [
                            {
                                "is_mobile": True,
                                "phone_number": item.cell_pone,
                                "is_active": True,
                                "mebbco_type": "fund",
                                "customer": customer
                            },
                            {
                                "phone_number": item.phone,
                                "mebbco_type": "fund",
                                "customer": customer
                            },
                    ]:
                        CustomerPhonePerson.objects.get_or_create(**phone)
                    print(item)
