from django_grpc_framework import proto_serializers
from base.models import BaseProvince
from service.server.grpc import province_pb2


class ProvinceProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = BaseProvince
        proto_class = province_pb2.BaseProvince
        fields = ["id", "name", "rayan_province_id"]
