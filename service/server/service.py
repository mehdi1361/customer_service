import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from base.models import BaseBank, BaseProvince, BaseCities, BaseBankBranch, \
    BaseCities, BaseState
from service.server.serializers import BankProtoSerializer, \
    ProvinceProtoSerializer, CityProtoSerializer, \
    CustomerComexVisitorProtoSerializer, CustomerProtoSerializer, \
    CustomerActiveMobileProtoSerializer, SejamRegisterPrivatePersonSerializer, \
    SejamRegisterPrivatePersonResponseSerializer, \
    GetStateSerializer, SetStateResponseSerializer, CustomerJobInfoSerializer
from django_grpc_framework import generics
from customer.models import CustomerComexVisitor, Customer, CustomerPhonePerson, \
    CustomerFinancialInfo, CustomerJobInfo, CustomerBankAccount, \
    CustomerAddress, CustomerPrivateInfo, CustomerState, CustomerJobInfo
from django.db import transaction
from service.server.grpc import customer_pb2



class BankService(Service):
    def List(self, request, context):
        banks = BaseBank.objects.all()
        serializer = BankProtoSerializer(banks, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        serializer = BankProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        try:
            return BaseBank.objects.get(pk=pk)
        except BaseBank.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Post:%s not found!' % pk)

    def Retrieve(self, request, context):
        bank = self.get_object(request.id)
        serializer = BankProtoSerializer(bank)
        return serializer.message

    def Update(self, request, context):
        bank = self.get_object(request.id)
        serializer = BankProtoSerializer(bank, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        bank = self.get_object(request.id)
        bank.delete()
        return empty_pb2.Empty()


class ProvinceService(generics.ModelService):
   queryset = BaseProvince.objects.all()
   serializer_class = ProvinceProtoSerializer


class CityService(generics.ModelService):
   queryset = BaseCities.objects.all()
   serializer_class = CityProtoSerializer


class CustomerComexVisitorService(generics.ModelService):
   queryset = CustomerComexVisitor.objects.all()
   serializer_class = CustomerComexVisitorProtoSerializer



class CustomerService(Service):
    def List(self, request, context):
        customers = Customer.objects.all()
        serializer = CustomerProtoSerializer(customers, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        serializer = CustomerProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, national_code):
        try:
            return Customer.objects.get(normal_national_code=national_code)
        except Customer.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'customer:%s not found!' % national_code)

    def Retrieve(self, request, context):
        customer = self.get_object(request.national_code)
        serializer = CustomerProtoSerializer(customer)
        return serializer.message

    def Update(self, request, context):
        customer = self.get_object(request.national_code)
        serializer = CustomerProtoSerializer(customer, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        customer = self.get_object(request.national_code)
        customer.delete()
        return empty_pb2.Empty()

    def GetActiveMobile(self, request, context):
        customer = self.get_object(request.national_code)
        actiive_mobile = CustomerPhonePerson.objects.filter(
            customer=customer,
            is_active=True
        ).first()
        serializer = CustomerActiveMobileProtoSerializer(actiive_mobile)
        return serializer.message

    def SejamRegisterPrivatePerson(self, request, context):
        with transaction.atomic():
            customer, _ =Customer.objects.get_or_create(
                normal_national_code=request.profile.normal_national_code,
                defaults= {
                    "sejam_type": request.profile.sejam_type,
                    "is_sejami": True
                }
            )



            CustomerFinancialInfo.objects.get_or_create(
                customer=customer,
                defaults= {
                    "asset_value": request.financial_info.assets_value,
                    "incoming_average": request.financial_info.incoming_average,
                    "s_exchange_tranasction": request.financial_info.s_exchange_transaction,
                    "c_exchange_tranasction": request.financial_info.c_exchange_transaction,
                    "out_exchange_tranasction": request.financial_info.out_exchange_transaction,
                    "tranasction_level": request.financial_info.transaction_level,
                    "trading_knowledge_level": request.financial_info.trading_knowledge_level,
                    "company_purpose": request.financial_info.company_purpose,
                    "reference_rate_company": request.financial_info.reference_rate_company,
                    "rate_date": request.financial_info.rate_date,
                    "rate": request.financial_info.rate
                }
            )

            CustomerJobInfo.objects.get_or_create(
                customer=customer,
                defaults={
                    "employment_date": request.job_info.employment_date,
                    "company_name": request.job_info.company_name,
                    "company_address": request.job_info.company_address,
                    "company_postal_code": request.job_info.company_postal_code,
                    "company_email": request.job_info.company_email,
                    "company_website": request.job_info.company_website,
                    "company_city_prefix": request.job_info.company_city_prefix,
                    "company_phone": request.job_info.company_phone,
                    "position": request.job_info.position,
                    "company_fax_prefix": request.job_info.company_fax_prefix,
                    "company_fax": request.job_info.company_fax,
                  #  "job": request.job_info.job_id,
                    "job_title": request.job_info.job_title,
                    "job_description": request.job_info.job_description

                }
            )
            for item in request.sejam_bank_accounts:
                city, _ = BaseCities.objects.get_or_create(
                    sejam_id=item.branch_city_id,
                    name=item.branch_city_name
                )

                bank, _ = BaseBank.objects.get_or_create(
                    title=item.bank_name,
                    sejam_id=item.bank_id
                )

                branch, _ = BaseBankBranch.objects.get_or_create(
                    code=item.branch_code,
                    city=city,
                    bank=bank,
                    defaults={
                        "name": item.branch_name,

                    }
                )
                CustomerBankAccount.objects.get_or_create(
                    customer=customer,
                    account_number=item.account_number,
                    defaults={
                        "ba_type_name": item.account_type,
                        "sheba": item.sheba,
                        "branch":branch
                    }
                )


        for item in request.sejam_addresses:
            CustomerAddress.objects.get_or_create(
                postal_code=item.postal_code,
                customer=customer,
                defaults={
                    "address": item.remnant_address,
                    "country_id": item.country_id,
                    "country_name": item.country_name,
                    "province_id": item.province_id,
                    "province_name": item.province_name,
                    "city_id": item.city_id,
                    "city_name": item.city_name,
                    "section_id": item.section_id,
                    "section_name": item.section_name,
                    "city_prefix": item.city_prefix,
                    "alley": item.alley,
                    "plaque": item.plaque,
                    "tel": item.tel,
                    "country_prefix": item.country_prefix,
                    "mobile":item.mobile,
                    "emergency_tel": item.emergency_tel,
                    "emergency_tel_city_prefix": item.emergency_tel_city_prefix,
                    "emergency_tel_country_prefix": item.emergency_tel_country_prefix,
                    "fax_prefix": item.fax_prefix,
                    "fax": item.fax,
                    "website": item.website,
                    "email": item.email
                }

            )
            CustomerPhonePerson.objects.get_or_create(
                phone_number=item.mobile,
                customer=customer,
                defaults={
                    "is_active": True,
                    "is_mobile": True
                }
            )

        CustomerPrivateInfo.objects.get_or_create(
            id=customer,
            defaults= {
                "first_name": request.private_person.first_name,
                "last_name": request.private_person.last_name,
                "father_name": request.private_person.father_name,
                "gender": request.private_person.gender,
                "seri_sh_char": request.private_person.seri_sh_char,
                "seri_sh": request.private_person.seri_sh,
                "serial": request.private_person.serial,
                "sh_number": request.private_person.sh_number,
                "birth_date": request.private_person.birth_date,
                "place_of_issue": request.private_person.place_of_issue,
                "place_of_birth": request.private_person.place_of_birth,
            }
        )
        result = customer_pb2.SejamRegisterPrivatePersonResponse(id=200, message="اطلاعات با موفقیت ذخیره  شد")
        response_serializer = SejamRegisterPrivatePersonResponseSerializer(result)
        return response_serializer.message


    def GetState(self, request, context):
        result = []
        import ipdb; ipdb.set_trace()
        for item in BaseState.objects.all():
            c = CustomerState.objects.filter(
                customer__normal_national_code=request.normal_national_code,
                state=item
            ).first()
            result.append(customer_pb2.State(
                state_name=item.state_name,
                title=item.title,
                icon_class=item.icon_class,
                state_id=item.state_id,
                confirm=c.confirm if c is not None else False
            ))

        response_serialzer = GetStateSerializer(result, many=True)
        return response_serialzer.message


    def SetState(self, request, context):
        state = BaseState.objects.get(id=request.state_id)
        customer = Customer.objects.get(id=request.normal_national_code)

        customer_state, _ = CustomerState.objects.get_or_create(
            customer=customer,
            state=state
        )
        customer_state.confirm=request.confirm
        customer_state.save()

        result = customer_pb2.SetStateResponse(id=200, message="وضعیت با تغییر یافت")
        response_serializer = SetStateResponseSerializer(result)
        return response_serializer.message

    def GetPersonJobInfo(self, request, context):
        customer = self.get_object(request.national_code)
        jobs = CustomerJobInfo.objects.filter(
            customer=customer,
            is_active=True
        ).first()

        serializer = CustomerJobInfoSerializer(jobs, many=True)
        return serializer.message
