
from django_grpc_framework import proto_serializers
from customer.models import Customer
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
