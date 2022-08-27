# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from service.server.grpc import bank_pb2 as bank__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class BaseBankControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/bank.BaseBankController/List',
                request_serializer=bank__pb2.BaseBankListRequest.SerializeToString,
                response_deserializer=bank__pb2.BaseBank.FromString,
                )
        self.Create = channel.unary_unary(
                '/bank.BaseBankController/Create',
                request_serializer=bank__pb2.BaseBank.SerializeToString,
                response_deserializer=bank__pb2.BaseBank.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/bank.BaseBankController/Retrieve',
                request_serializer=bank__pb2.BaseBankRetrieveRequest.SerializeToString,
                response_deserializer=bank__pb2.BaseBank.FromString,
                )
        self.Update = channel.unary_unary(
                '/bank.BaseBankController/Update',
                request_serializer=bank__pb2.BaseBank.SerializeToString,
                response_deserializer=bank__pb2.BaseBank.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/bank.BaseBankController/Destroy',
                request_serializer=bank__pb2.BaseBank.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class BaseBankControllerServicer(object):
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


def add_BaseBankControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=bank__pb2.BaseBankListRequest.FromString,
                    response_serializer=bank__pb2.BaseBank.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=bank__pb2.BaseBank.FromString,
                    response_serializer=bank__pb2.BaseBank.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=bank__pb2.BaseBankRetrieveRequest.FromString,
                    response_serializer=bank__pb2.BaseBank.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=bank__pb2.BaseBank.FromString,
                    response_serializer=bank__pb2.BaseBank.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=bank__pb2.BaseBank.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bank.BaseBankController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BaseBankController(object):
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
        return grpc.experimental.unary_stream(request, target, '/bank.BaseBankController/List',
            bank__pb2.BaseBankListRequest.SerializeToString,
            bank__pb2.BaseBank.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/bank.BaseBankController/Create',
            bank__pb2.BaseBank.SerializeToString,
            bank__pb2.BaseBank.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/bank.BaseBankController/Retrieve',
            bank__pb2.BaseBankRetrieveRequest.SerializeToString,
            bank__pb2.BaseBank.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/bank.BaseBankController/Update',
            bank__pb2.BaseBank.SerializeToString,
            bank__pb2.BaseBank.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/bank.BaseBankController/Destroy',
            bank__pb2.BaseBank.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
