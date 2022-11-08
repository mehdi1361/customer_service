import grpc

from datetime import datetime, timezone
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from base.models import BaseBank, BaseProvince, BaseCities, BaseBankBranch, \
    BaseCities, BaseState, BaseFileType, BaseFund
from service.server.serializers import BankProtoSerializer, \
    ProvinceProtoSerializer, CityProtoSerializer, \
    CustomerComexVisitorProtoSerializer, CustomerProtoSerializer, \
    CustomerActiveMobileProtoSerializer, SejamRegisterPrivatePersonSerializer, \
    SejamRegisterPrivatePersonResponseSerializer, \
    GetStateSerializer, SetStateResponseSerializer, CustomerJobInfoSerializer, \
    CustomerAddressInfoSerializer, \
    CustomerFinancialInfoInfoSerializer, CustomerFileSerializer, \
    PostCustomerFileSerializer, CustomerInfoSerializer, AccountSerializer, \
    LoginByNationalResponseSerializer, CustomerVerifiedSerializer, CustomerAppSerializer
from django_grpc_framework import generics
from customer.models import CustomerComexVisitor, Customer, CustomerPhonePerson, \
    CustomerFinancialInfo, CustomerJobInfo, CustomerBankAccount, \
    CustomerAddress, CustomerPrivateInfo, CustomerState, CustomerJobInfo, \
    CustomerFile, CustomerVerification, CustomerFund
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
            self.context.abort(grpc.StatusCode.NOT_FOUND,
                               'Post:%s not found!' % pk)

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
            self.context.abort(grpc.StatusCode.NOT_FOUND,
                               'customer:%s not found!' % national_code)

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
            customer, _ = Customer.objects.get_or_create(
                normal_national_code=request.profile.normal_national_code,
                defaults={
                    "sejam_type": request.profile.sejam_type,
                    "is_sejami": True
                }
            )

            CustomerFinancialInfo.objects.get_or_create(
                customer=customer,
                defaults={
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
                        "branch": branch
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
                    "mobile": item.mobile,
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
            defaults={
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
        result = customer_pb2.SejamRegisterPrivatePersonResponse(
            id=200, message="اطلاعات با موفقیت ذخیره  شد")
        response_serializer = SejamRegisterPrivatePersonResponseSerializer(
            result)
        return response_serializer.message

    def GetCustomerState(self, request, context):
        customer = self.get_object(request.national_code)

        result = []
        for item in BaseState.objects.all():
            c = CustomerState.objects.filter(
                customer=customer,
                state=item
            ).first()
            result.append(customer_pb2.CustomerStateResponse(
                state_name=item.state_name,
                title=item.title,
                icon_class=item.icon_class,
                state_id=item.state_id,
                confirm=c.confirm if c is not None else False
            ))

        response_serialzer = GetStateSerializer(result, many=True)

        for msg in response_serialzer.message:
            yield msg

    def SetState(self, request, context):
        state = BaseState.objects.get(id=request.state_id)
        customer = Customer.objects.get(
            normal_national_code=request.normal_national_code)

        customer_state, _ = CustomerState.objects.get_or_create(
            customer=customer,
            state=state
        )
        customer_state.confirm = request.confirm
        customer_state.save()

        result = customer_pb2.SetStateResponse(
            id=200, message="وضعیت با تغییر یافت")
        response_serializer = SetStateResponseSerializer(result)
        return response_serializer.message

    def GetPersonJobInfo(self, request, context):
        customer = self.get_object(request.normal_national_code)
        job = CustomerJobInfo.objects.get(
            customer=customer
        )

        serializer = CustomerJobInfoSerializer(job)
        return serializer.message

    def GetPersonByAddress(self, request, context):
        customer = self.get_object(request.normal_national_code)
        address = CustomerAddress.objects.get(customer=customer)
        serializer = CustomerAddressInfoSerializer(address)
        return serializer.message

    def GetPersonBankAccount(self, request, context):
        customer = self.get_object(request.normal_national_code)
        accounts = CustomerBankAccount.objects.select_related(
            'branch').filter(customer=customer)
        result = []
        for account in accounts:
            result.append(customer_pb2.Account(
                rayan_bank_account_id=account.rayan_bank_account_id,
                account_number=account.account_number,
                ba_type_name=account.ba_type_name,
                is_default=True if account.is_default is not None else False,
                is_active=True if account.is_active is not None else False,
                is_online=True if account.is_online is not None else False,
                sheba=account.sheba,
                branch_name=account.branch.name,
                branch_code=account.branch.code,
                dl_number=account.branch.dl_number,
                bank=account.branch.bank.title,
                city=account.branch.city.name
            ))
        serializer = AccountSerializer(result, many=True)
        for message in serializer.message:
            yield message

    def GetPersonFinancialInfo(self, request, context):
        customer = self.get_object(request.normal_national_code)
        financial_info = CustomerFinancialInfo.objects.filter(
            customer=customer).first()
        serializer = CustomerFinancialInfoInfoSerializer(financial_info)
        return serializer.message

    def CustomerGetFile(self, request, context):
        customer = self.get_object(request.normal_national_code)
        result = []
        for item in BaseFileType.objects.all():
            c_file = CustomerFile.objects.filter(
                customer=customer, file_type=item).first()
            result.append(customer_pb2.CustomerFile(
                id=item.id,
                name=item.name,
                fa_name=item.fa_name,
                is_force=item.is_force,
                file_data=None if c_file is None else c_file.file_data,
                extension_name="image/jpg, image/jpeg, image/png",
                extension_real_size=5*1024*1024,
                extension_size="5MB"
            ))

        for message in CustomerFileSerializer(result, many=True).message:
            yield message

    def CustomerPostFile(self, request, context):
        try:
            customer = self.get_object(request.normal_national_code)
            file_type = BaseFileType.objects.get(name=request.file_type_name)
            c, created = CustomerFile.objects.get_or_create(
                customer=customer,
                file_type=file_type,
                defaults={"file_data": request.file_data}
            )
            if not created:
                c.file_data = request.file_data
                c.save()

            result = customer_pb2.PostCustomerFileResponse(
                id=200, message="اطلاعات با موفقیت ذخیره  شد")
        except Exception as e:
            result = customer_pb2.PostCustomerFileResponse(
                id=400, message="خطا در ثبت اطلاعات")

        finally:
            response_serializer = PostCustomerFileSerializer(result)
            return response_serializer.message

    def GetPersonByNationalId(self, request, context):
        customer = self.get_object(request.normal_national_code)
        info = CustomerPrivateInfo.objects.filter(id=customer).first()

        result = customer_pb2.PersonByNationalIdResponse(
            first_name=info.first_name,
            last_name=info.last_name,
            father_name=info.father_name,
            seri_sh_char=info.seri_sh_char,
            seri_sh=info.seri_sh,
            serial=info.serial,
            sh_number=info.sh_number,
            birth_date=info.birth_date,
            place_of_issue=info.place_of_issue,
            place_of_birth=info.place_of_birth,
            economic_code="",
            national_id=customer.normal_national_code,
        )
        response_serializer = CustomerInfoSerializer(result)
        return response_serializer.message

    def LoginByNationalId(self, request, context):
        customer = self.get_object(request.normal_national_code)
        phones = CustomerPhonePerson.objects.filter(
            customer=customer,
            is_mobile=True,
            is_active=True
        )

        if phones.count() > 1:
            result = customer_pb2.LoginStateResponse(
                id=403,
                message="تلفن های همراه فعال بیش از یک عدد است"
            )
            response_serializer = LoginByNationalResponseSerializer(result)
            return response_serializer.message

        result_data = CustomerVerification.send_verification_code(
            customer, phones.first())
        result = customer_pb2.LoginStateResponse(
            id=result_data.status_code,
            message="کد فعال سازی ارسال شد" if result_data.status_code == 200 else "خطا در ارسال پیامک"
        )
        response_serializer = LoginByNationalResponseSerializer(result)
        return response_serializer.message

    def CustomerVerified(self, request, context):
        customer = self.get_object(request.normal_national_code)
        verified = CustomerVerification.objects.filter(
            customer=customer,
            is_active=True
        ).first()

        def message(data):
            result = customer_pb2.StateResponse(**data)
            response_serializer = CustomerVerifiedSerializer(result)
            return response_serializer.message

        if verified is None:
            return message({
                "id": 404,
                "message": "کد فعالسازی یافت نشد"
            })

        now = datetime.now(timezone.utc)
        if (now - verified.created_date) / 60 > 2:
            verified.is_active = False
            verified.save()
            return message({
                "id": 403,
                "message": "کد فعالسازی منقضی شده است"
            })

        if verified.code != request.verification_code:
            return message({
                "id": 400,
                "message": "کد فعالسازی اشتباه است"
            })

        verified.is_active = False
        verified.save()
        return message({"id": 200, "message": "کد فعالسازی تایید شد"})


    def CustomerListApp(self, request, context):
        customer = self.get_object(request.normal_national_code)
        result = []


        for item in BaseFund.objects.all():
            result.append(
                customer_pb2.CustomerApp(
                    id=item.id,
                    name=item.name,
                    fa_name=item.fa_name,
                    active=CustomerFund.objects.filter(customer_service=customer, fund=item).exists()
                )
            )

        serializer = CustomerAppSerializer(result, many=True)
        for msg in serializer.message:
            yield msg
