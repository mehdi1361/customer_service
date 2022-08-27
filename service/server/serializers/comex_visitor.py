from django_grpc_framework import proto_serializers
from customer.models import CustomerComexVisitor
from service.server.grpc import customer_comex_visitor_pb2
from rest_framework import serializers

class CustomerComexVisitorProtoSerializer(
        proto_serializers.ModelProtoSerializer
):

    class Meta:
        model = CustomerComexVisitor
        proto_class = customer_comex_visitor_pb2.CustomerComexVisitor
        fields = ["id", "comex_id_rayan", "full_name", "rate", "type_mebbco"]
