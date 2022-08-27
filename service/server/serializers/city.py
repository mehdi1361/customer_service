from django_grpc_framework import proto_serializers
from base.models import BaseCities
from service.server.grpc import city_pb2
from rest_framework import serializers

class CityProtoSerializer(proto_serializers.ModelProtoSerializer):
    province = serializers.SerializerMethodField()

    class Meta:
        model = BaseCities
        proto_class = city_pb2.BaseCities
        fields = ["id", "name", "province", "rayan_city_id"]

    def get_province(self, obj):
        return obj.province.name
