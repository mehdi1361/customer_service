import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from base.models import BaseBank, BaseProvince, BaseCities
from service.server.serializers import BankProtoSerializer, \
    ProvinceProtoSerializer, CityProtoSerializer, \
    CustomerComexVisitorProtoSerializer, CustomerProtoSerializer, \
    CustomerActiveMobileProtoSerializer, SejamRegisterPrivatePersonSerializer, \
    SejamRegisterPrivatePersonResponseSerializer
from django_grpc_framework import generics
from customer.models import CustomerComexVisitor, Customer, CustomerPhonePerson


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


#class CustomerService(generics.ModelService):
#   queryset = Customer.objects.all()
#   serializer_class = CustomerProtoSerializer


class CustomerService(Service):
    def List(self, request, context):
        banks = Customer.objects.all()
        serializer = CustomerProtoSerializer(banks, many=True)
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
        serializer = SejamRegisterPrivatePersonSerializer
        print(serializer)
        response_serializer = SejamRegisterPrivatePersonResponseSerializer(
            id=200,
            message="ok"
        )
        return response_serializer.message
