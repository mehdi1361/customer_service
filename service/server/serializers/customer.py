
from django_grpc_framework import proto_serializers
from customer.models import Customer, \
    CustomerPhonePerson, CustomerFinancialInfo, CustomerJobInfo, \
    CustomerBankAccount, CustomerAddress, CustomerPrivateInfo, \
    CustomerState, CustomerJobInfo, CustomerAddress, \
    CustomerBankAccount, CustomerFinancialInfo
from service.server.grpc import customer_pb2
from rest_framework import serializers
from base.models import BaseState, BaseBankBranch


class CustomerProtoSerializer(
        proto_serializers.ModelProtoSerializer
):

    class Meta:
        model = Customer
        proto_class = customer_pb2.Customer
        fields = [
            "id",
            "sejam_reference_code",
            "normal_national_code",
            "user_name",
            "is_active",
            "is_sejami",
            "is_rayan_service",
            "sejam_type",
            "rayan_customer_id",
        ]


class CustomerActiveMobileProtoSerializer(
        proto_serializers.ModelProtoSerializer
):

    class Meta:
        model = CustomerPhonePerson
        proto_class = customer_pb2.CustomerPhone
        fields = [
            "phone_number",
            "is_active",
            "is_mobile",
            "mebbco_type",
        ]


class SejamProfileSerializer(
        proto_serializers.ModelProtoSerializer
):
    class Meta:
        model = Customer
        proto_class = customer_pb2.SejamProfileParams
        fields = [
            "normal_national_code",
            "email_address",
            "sejam_type",
            "is_sejami",
            "is_active"
        ]

class SejamFinancialInfoSerializer(
        proto_serializers.ModelProtoSerializer
):
    model = CustomerFinancialInfo
    proto_class = customer_pb2.SejamProfileParams
    fields = [
        "assets_value",
        "incoming_average",
        "s_exchange_transaction",
        "c_exchange_transaction",
        "out_exchange_transaction",
        "transaction_level",
        "trading_knowledge_level",
        "company_purpose",
        "reference_rate_company",
        "rate_date",
        "rate",
    ]


class SejamJobInfoSerializer(
        proto_serializers.ModelProtoSerializer
):

    model = CustomerJobInfo
    proto_class = customer_pb2.SejamJobInfo
    fields = [
        "employment_date",
        "company_name",
        "company_address",
        "company_postal_code",
        "company_email",
        "company_website",
        "company_city_prefix",
        "company_phone",
        "position",
        "company_fax_prefix",
        "company_fax",
        "job_id",
        "job_title",
        "job_description",
    ]


class SejamBankAccountSerializer(
        proto_serializers.ModelProtoSerializer
):

    model = CustomerBankAccount
    proto_class = customer_pb2.SejamBankAccount
    fields = [
        "account_number",
        "account_type",
        "sheba",
        "bank_id",
        "bank_name",
        "branch_code",
        "branch_name",
        "branch_city_id",
        "branch_city_name",
        "is_default",
    ]


class SejamAddressSerializer(
        proto_serializers.ModelProtoSerializer
):

    model = CustomerAddress
    proto_class = customer_pb2.SejamAddress
    fields = [
        "country_id",
        "country_name",
        "province_id",
        "province_name",
        "city_id",
        "city_name",
        "section_id",
        "section_name",
        "city_prefix",
        "remnant_address",
        "alley",
        "plaque",
        "tel",
        "country_prefix",
        "mobile",
        "emergency_tel",
        "emergency_tel_city_prefix",
        "emergency_tel_country_prefix",
        "fax_prefix",
        "fax",
        "website",
        "email",
        "postal_code",
    ]


class SejamPrivatePersonSerializer(
        proto_serializers.ModelProtoSerializer
):

    model = CustomerPrivateInfo
    proto_class = customer_pb2.SejamPrivatePerson
    fields = [
        "first_name",
        "last_name",
        "father_name",
        "gender",
        "seri_sh_char",
        "seri_sh",
        "serial",
        "sh_number",
        "birth_date",
        "place_of_issue",
        "place_of_birth",
        "signature_file",
    ]


class SejamRegisterPrivatePersonSerializer(
        proto_serializers.ProtoSerializer
):
    profile = SejamProfileSerializer()
    financial_info = SejamFinancialInfoSerializer()
    job_info = SejamJobInfoSerializer()
    sejam_bank_accounts = SejamBankAccountSerializer(many=True)
    sejam_addresses = SejamAddressSerializer(many=True)
    private_person = SejamPrivatePersonSerializer()


#    fields = [
#        "profile",
#        "financial_info",
#        "job_info",
#        "sejam_bank_accounts",
#        "sejam_addresses",
#        "private_person",
#    ]

    class Meta:
        proto_class = customer_pb2.SejamRegisterPrivatePersonRequest


class SejamRegisterPrivatePersonResponseSerializer(
        proto_serializers.ProtoSerializer
):
    id =  serializers.IntegerField()
    message = serializers.CharField(max_length=100)

    class Meta:

        proto_class = customer_pb2.SejamRegisterPrivatePersonResponse


class GetStateSerializer(
        proto_serializers.ProtoSerializer
):
    state_name = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    icon_class = serializers.CharField(max_length=100)
    state_id = serializers.CharField(max_length=100)
    confirm = serializers.BooleanField()

    class Meta:
        proto_class = customer_pb2.State


class SetStateResponseSerializer(
        proto_serializers.ProtoSerializer
):
    id =  serializers.IntegerField()
    message = serializers.CharField(max_length=100)

    class Meta:

        proto_class = customer_pb2.SetStateResponse


class CustomerJobInfoSerializer(
        proto_serializers.ModelProtoSerializer
):

    model = CustomerJobInfo
    proto_class = customer_pb2.SejamJobInfo
    fields = [
        "employment_date",
        "company_name",
        "company_address",
        "company_postal_code",
        "company_email",
        "company_website",
        "company_city_prefix",
        "company_phone",
        "position",
        "company_fax_prefix",
        "company_fax",
        "job_id",
        "job_title",
        "job_description",
        "customer_id",
    ]


class CustomerAddressInfoSerializer(
        proto_serializers.ModelProtoSerializer
):

    model = CustomerAddress
    proto_class = customer_pb2.PersonByAddressResponse
    fields = [
        "postal_code",
        "address",
        "mobile",
        "fax",
        "tel",
        "email",
        "province_name",
        "city_name",
    ]

class BranchDataSerializer(
        proto_serializers.ModelProtoSerializer
):
    model = BaseBankBranch
    proto_class = customer_pb2.BranchData

class CustomerAddressInfoSerializer(
        proto_serializers.ModelProtoSerializer
):

    model = CustomerBankAccount
    proto_class = customer_pb2.PersonBankAccount
    fields = [
        "account_number",
        "rayan_bank_account_id",
        "ba_type_name",
        "shaba",
        "is_default",
        "is_active",
        "is_online",
        "branch_data",
    ]



class CustomerBranchDataSerializer(
        proto_serializers.ModelProtoSerializer
):
    model = BaseBankBranch
    proto_class = customer_pb2.BranchData
    fields = [
        "name",
        "code",
        "sejam_code",
        "dl_number",
        "bank",
        "city",
    ]

class CustomerBankAccountInfoInfoSerializer(
        proto_serializers.ModelProtoSerializer
):

    branch_data = BranchDataSerializer(read_only=True)
    model = CustomerBankAccount
    proto_class = customer_pb2.PersonBankAccount
    fields = [
        "account_number",
        "rayan_bank_account_id",
        "ba_type_name",
        "shaba",
        "is_default",
        "is_active",
        "is_online",
        "branch_data",
    ]

class CustomerFinancialInfoInfoSerializer(
        proto_serializers.ModelProtoSerializer
):

    model = CustomerFinancialInfo
    proto_class = customer_pb2.PersonBankAccount
    fields = [
        "account_number",
        "rayan_bank_account_id",
        "ba_type_name",
        "shaba",
        "is_default",
        "is_active",
        "is_online",
        "branch_data",
    ]
