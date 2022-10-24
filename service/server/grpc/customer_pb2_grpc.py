# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from service.server.grpc import customer_pb2 as customer__pb2


class CustomerControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/customer.CustomerController/List',
                request_serializer=customer__pb2.CustomerListRequest.SerializeToString,
                response_deserializer=customer__pb2.Customer.FromString,
                )
        self.Create = channel.unary_unary(
                '/customer.CustomerController/Create',
                request_serializer=customer__pb2.Customer.SerializeToString,
                response_deserializer=customer__pb2.Customer.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/customer.CustomerController/Retrieve',
                request_serializer=customer__pb2.CustomerRetrieveRequest.SerializeToString,
                response_deserializer=customer__pb2.Customer.FromString,
                )
        self.Update = channel.unary_unary(
                '/customer.CustomerController/Update',
                request_serializer=customer__pb2.Customer.SerializeToString,
                response_deserializer=customer__pb2.Customer.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/customer.CustomerController/Destroy',
                request_serializer=customer__pb2.Customer.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetActiveMobile = channel.unary_unary(
                '/customer.CustomerController/GetActiveMobile',
                request_serializer=customer__pb2.CustomerRetrieveRequest.SerializeToString,
                response_deserializer=customer__pb2.CustomerPhone.FromString,
                )
        self.SejamRegisterPrivatePerson = channel.unary_unary(
                '/customer.CustomerController/SejamRegisterPrivatePerson',
                request_serializer=customer__pb2.SejamRegisterPrivatePersonRequest.SerializeToString,
                response_deserializer=customer__pb2.SejamRegisterPrivatePersonResponse.FromString,
                )
        self.GetCustomerState = channel.unary_stream(
                '/customer.CustomerController/GetCustomerState',
                request_serializer=customer__pb2.CustomerStateRequest.SerializeToString,
                response_deserializer=customer__pb2.CustomerStateResponse.FromString,
                )
        self.SetState = channel.unary_unary(
                '/customer.CustomerController/SetState',
                request_serializer=customer__pb2.SetStateRequest.SerializeToString,
                response_deserializer=customer__pb2.SetStateResponse.FromString,
                )
        self.GetPersonJobInfo = channel.unary_unary(
                '/customer.CustomerController/GetPersonJobInfo',
                request_serializer=customer__pb2.PersonByNationalIdRequest.SerializeToString,
                response_deserializer=customer__pb2.JobInfoResponse.FromString,
                )
        self.GetPersonByNationalId = channel.unary_unary(
                '/customer.CustomerController/GetPersonByNationalId',
                request_serializer=customer__pb2.PersonByNationalIdRequest.SerializeToString,
                response_deserializer=customer__pb2.PersonByNationalIdResponse.FromString,
                )
        self.GetPersonByAddress = channel.unary_unary(
                '/customer.CustomerController/GetPersonByAddress',
                request_serializer=customer__pb2.PersonByNationalIdRequest.SerializeToString,
                response_deserializer=customer__pb2.PersonByAddressResponse.FromString,
                )
        self.GetPersonBankAccount = channel.unary_stream(
                '/customer.CustomerController/GetPersonBankAccount',
                request_serializer=customer__pb2.PersonByNationalIdRequest.SerializeToString,
                response_deserializer=customer__pb2.Account.FromString,
                )
        self.GetPersonFinancialInfo = channel.unary_unary(
                '/customer.CustomerController/GetPersonFinancialInfo',
                request_serializer=customer__pb2.PersonByNationalIdRequest.SerializeToString,
                response_deserializer=customer__pb2.PersonFinancialResponse.FromString,
                )
        self.CustomerGetFile = channel.unary_stream(
                '/customer.CustomerController/CustomerGetFile',
                request_serializer=customer__pb2.PersonByNationalIdRequest.SerializeToString,
                response_deserializer=customer__pb2.CustomerFile.FromString,
                )
        self.CustomerPostFile = channel.unary_unary(
                '/customer.CustomerController/CustomerPostFile',
                request_serializer=customer__pb2.PostCustomerFile.SerializeToString,
                response_deserializer=customer__pb2.PostCustomerFileResponse.FromString,
                )


class CustomerControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActiveMobile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SejamRegisterPrivatePerson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomerState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPersonJobInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPersonByNationalId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPersonByAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPersonBankAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPersonFinancialInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CustomerGetFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CustomerPostFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CustomerControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=customer__pb2.CustomerListRequest.FromString,
                    response_serializer=customer__pb2.Customer.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=customer__pb2.Customer.FromString,
                    response_serializer=customer__pb2.Customer.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=customer__pb2.CustomerRetrieveRequest.FromString,
                    response_serializer=customer__pb2.Customer.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=customer__pb2.Customer.FromString,
                    response_serializer=customer__pb2.Customer.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=customer__pb2.Customer.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetActiveMobile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActiveMobile,
                    request_deserializer=customer__pb2.CustomerRetrieveRequest.FromString,
                    response_serializer=customer__pb2.CustomerPhone.SerializeToString,
            ),
            'SejamRegisterPrivatePerson': grpc.unary_unary_rpc_method_handler(
                    servicer.SejamRegisterPrivatePerson,
                    request_deserializer=customer__pb2.SejamRegisterPrivatePersonRequest.FromString,
                    response_serializer=customer__pb2.SejamRegisterPrivatePersonResponse.SerializeToString,
            ),
            'GetCustomerState': grpc.unary_stream_rpc_method_handler(
                    servicer.GetCustomerState,
                    request_deserializer=customer__pb2.CustomerStateRequest.FromString,
                    response_serializer=customer__pb2.CustomerStateResponse.SerializeToString,
            ),
            'SetState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetState,
                    request_deserializer=customer__pb2.SetStateRequest.FromString,
                    response_serializer=customer__pb2.SetStateResponse.SerializeToString,
            ),
            'GetPersonJobInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPersonJobInfo,
                    request_deserializer=customer__pb2.PersonByNationalIdRequest.FromString,
                    response_serializer=customer__pb2.JobInfoResponse.SerializeToString,
            ),
            'GetPersonByNationalId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPersonByNationalId,
                    request_deserializer=customer__pb2.PersonByNationalIdRequest.FromString,
                    response_serializer=customer__pb2.PersonByNationalIdResponse.SerializeToString,
            ),
            'GetPersonByAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPersonByAddress,
                    request_deserializer=customer__pb2.PersonByNationalIdRequest.FromString,
                    response_serializer=customer__pb2.PersonByAddressResponse.SerializeToString,
            ),
            'GetPersonBankAccount': grpc.unary_stream_rpc_method_handler(
                    servicer.GetPersonBankAccount,
                    request_deserializer=customer__pb2.PersonByNationalIdRequest.FromString,
                    response_serializer=customer__pb2.Account.SerializeToString,
            ),
            'GetPersonFinancialInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPersonFinancialInfo,
                    request_deserializer=customer__pb2.PersonByNationalIdRequest.FromString,
                    response_serializer=customer__pb2.PersonFinancialResponse.SerializeToString,
            ),
            'CustomerGetFile': grpc.unary_stream_rpc_method_handler(
                    servicer.CustomerGetFile,
                    request_deserializer=customer__pb2.PersonByNationalIdRequest.FromString,
                    response_serializer=customer__pb2.CustomerFile.SerializeToString,
            ),
            'CustomerPostFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CustomerPostFile,
                    request_deserializer=customer__pb2.PostCustomerFile.FromString,
                    response_serializer=customer__pb2.PostCustomerFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'customer.CustomerController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CustomerController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/customer.CustomerController/List',
            customer__pb2.CustomerListRequest.SerializeToString,
            customer__pb2.Customer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/Create',
            customer__pb2.Customer.SerializeToString,
            customer__pb2.Customer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/Retrieve',
            customer__pb2.CustomerRetrieveRequest.SerializeToString,
            customer__pb2.Customer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/Update',
            customer__pb2.Customer.SerializeToString,
            customer__pb2.Customer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/Destroy',
            customer__pb2.Customer.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActiveMobile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/GetActiveMobile',
            customer__pb2.CustomerRetrieveRequest.SerializeToString,
            customer__pb2.CustomerPhone.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SejamRegisterPrivatePerson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/SejamRegisterPrivatePerson',
            customer__pb2.SejamRegisterPrivatePersonRequest.SerializeToString,
            customer__pb2.SejamRegisterPrivatePersonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCustomerState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/customer.CustomerController/GetCustomerState',
            customer__pb2.CustomerStateRequest.SerializeToString,
            customer__pb2.CustomerStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/SetState',
            customer__pb2.SetStateRequest.SerializeToString,
            customer__pb2.SetStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPersonJobInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/GetPersonJobInfo',
            customer__pb2.PersonByNationalIdRequest.SerializeToString,
            customer__pb2.JobInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPersonByNationalId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/GetPersonByNationalId',
            customer__pb2.PersonByNationalIdRequest.SerializeToString,
            customer__pb2.PersonByNationalIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPersonByAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/GetPersonByAddress',
            customer__pb2.PersonByNationalIdRequest.SerializeToString,
            customer__pb2.PersonByAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPersonBankAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/customer.CustomerController/GetPersonBankAccount',
            customer__pb2.PersonByNationalIdRequest.SerializeToString,
            customer__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPersonFinancialInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/GetPersonFinancialInfo',
            customer__pb2.PersonByNationalIdRequest.SerializeToString,
            customer__pb2.PersonFinancialResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CustomerGetFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/customer.CustomerController/CustomerGetFile',
            customer__pb2.PersonByNationalIdRequest.SerializeToString,
            customer__pb2.CustomerFile.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CustomerPostFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerController/CustomerPostFile',
            customer__pb2.PostCustomerFile.SerializeToString,
            customer__pb2.PostCustomerFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
