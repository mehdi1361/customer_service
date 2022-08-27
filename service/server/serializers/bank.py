from django_grpc_framework import proto_serializers
from base.models import BaseBank
from service.server.grpc import bank_pb2


class BankProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = BaseBank
        proto_class = bank_pb2.BaseBank
        fields = ["id", "title"]
