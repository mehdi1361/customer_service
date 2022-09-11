
from django_grpc_framework import proto_serializers
from customer.models import Customer, \
    CustomerPhonePerson, CustomerFinancialInfo, CustomerJobInfo, \
    CustomerBankAccount, CustomerAddress, CustomerPrivateInfo
from service.server.grpc import customer_pb2
from rest_framework import serializers


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
    proto_class = customer_pb2.SejamRegisterPrivatePersonRequest
    fields = [
        "profile",
        "financial_info",
        "job_info",
        "sejam_bank_accounts",
        "sejam_addresses",
        "private_person",
    ]
