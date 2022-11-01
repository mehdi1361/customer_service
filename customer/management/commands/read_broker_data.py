from django.core.management.base import BaseCommand, CommandError
from service.client.rayan.broker_customer import customer_list

from customer.models import Customer, CustomerPrivateInfo,\
    CustomerBrokerInfo, CustomerPhonePerson, \
    CustomerBrokerBourseAccounts, CustomerBankAccount

from base.models import BaseProvince, BaseCities, BaseBankBranch, \
    BaseBank
from django.db import transaction

class Command(BaseCommand):
    help = 'read data from rayan'

    def handle(self, *args, **options):
        for item in customer_list().result:
            with transaction.atomic():
                obj, _ = Customer.objects.get_or_create(
                    normal_national_code=str(
                        item.nationalCode
                    ).replace("_", "").replace("-", ""),
                    defaults={
                        "rayan_customer_id": item.customerId,
                        "is_rayan_service": True
                    }
                )
                cp_obj, _ = CustomerPrivateInfo.objects.get_or_create(
                    id=obj,
                    defaults={
                        "first_name": item.firstName,
                        "last_name": item.lastName,
                        "father_name": item.fatherName,
                        "serial": item.birthCertificationNumber,
                        "sex_type_id": item.sexTypeId,
                        "sex_type_name": item.sexTypeName,
                    }
                )

                cb, _ = CustomerBrokerInfo.objects.get_or_create(
                    has_sign_sample=item.hasSignSample,
                    has_customer_photo=item.hasCustomerPhoto,
                    has_birth_certificate=item.hasBirthCertificate,
                    has_official_gazette=item.hasOfficialGazette,
                    has_official_ads=item.hasOfficialAds,
                    has_certificate_comments=item.hasCertificateComments,
                    has_online_account=item.hasOnlineAccount,
                    has_zip_file=item.hasZipFile,
                    customer_id=item.customerId,
                    telegram_status_id=item.telegramStatusId,
                    customer_service=obj,
                    bourse_account_name=item.bourseAccountName,
                    account_number=item.accountNumber,
                    is_site_user=item.isSiteUser,
                    comex_visitor_id=item.comexVisitorId,
                    comex_economy_account=item.comexEconomyAccount,
                    is_mmtp_user=item.isMmtpUser,
                    trader_credit=item.traderCredit,
                    mmtp_user_id=item.mmtpUserId,
                    customer_identity=item.customerIdentity,
                    is_stock_credit_purchase=item.isStockCreditPurchase,
                    is_collateral_stocks_customer=item.isCollateralStocksCustomer,
                    is_portfo=item.isPortfo,
                )

                for phone in [
                        {
                            "is_mobile": True,
                            "phone_number": item.mobileNumber,
                            "is_active": True,
                            "mebbco_type": "broker",
                            "customer": obj

                        },
                        {
                            "phone_number": item.phoneNumber,
                            "mebbco_type": "broker",
                            "customer": obj
                        },
                ]:
                    CustomerPhonePerson.objects.get_or_create(**phone)

                CustomerBrokerBourseAccounts.objects.get_or_create(
                    number=item.accountNumber,
                    name=item.bourseAccountName,
                    customer=cb
                )

                province, _ = BaseProvince.objects.get_or_create(
                    rayan_province_id=str(item.provinceCode),
                    defaults={"name": item.provinceName}
                )

                city, _ = BaseCities.objects.get_or_create(
                    rayan_city_id=str(item.cityCode),
                    defaults={
                        "name": item.cityName,
                        "province": province
                    }
                )
                bank, _ = BaseBank.objects.get_or_create(
                   title=item.bankName
                )

                branch, _ = BaseBankBranch.objects.get_or_create(
                    rayan_branch_id=item.branchId,
                    bank=bank,
                    defaults={
                        "name": item.branchName,
                        "city": city
                    }
                )

                customer_account, _ = CustomerBankAccount.objects.get_or_create(
                    sheba=item.shabaNumber,
                    defaults={
                        "branch": branch,
                        "account_number": item.bankAccountNumber,
                        "ba_type_name": item.baTypeName
                    }
                )


                print(item)
