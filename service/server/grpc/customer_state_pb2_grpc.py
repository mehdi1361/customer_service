# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from service.server.grpc import customer_state_pb2 as customer__state__pb2


class CustomerStateControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/customer_state.CustomerStateController/List',
                request_serializer=customer__state__pb2.CustomerStateListRequest.SerializeToString,
                response_deserializer=customer__state__pb2.CustomerState.FromString,
                )
        self.Create = channel.unary_unary(
                '/customer_state.CustomerStateController/Create',
                request_serializer=customer__state__pb2.CustomerState.SerializeToString,
                response_deserializer=customer__state__pb2.CustomerState.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/customer_state.CustomerStateController/Retrieve',
                request_serializer=customer__state__pb2.CustomerStateRetrieveRequest.SerializeToString,
                response_deserializer=customer__state__pb2.CustomerState.FromString,
                )
        self.Update = channel.unary_unary(
                '/customer_state.CustomerStateController/Update',
                request_serializer=customer__state__pb2.CustomerState.SerializeToString,
                response_deserializer=customer__state__pb2.CustomerState.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/customer_state.CustomerStateController/Destroy',
                request_serializer=customer__state__pb2.CustomerState.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class CustomerStateControllerServicer(object):
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


def add_CustomerStateControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=customer__state__pb2.CustomerStateListRequest.FromString,
                    response_serializer=customer__state__pb2.CustomerState.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=customer__state__pb2.CustomerState.FromString,
                    response_serializer=customer__state__pb2.CustomerState.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=customer__state__pb2.CustomerStateRetrieveRequest.FromString,
                    response_serializer=customer__state__pb2.CustomerState.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=customer__state__pb2.CustomerState.FromString,
                    response_serializer=customer__state__pb2.CustomerState.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=customer__state__pb2.CustomerState.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'customer_state.CustomerStateController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CustomerStateController(object):
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
        return grpc.experimental.unary_stream(request, target, '/customer_state.CustomerStateController/List',
            customer__state__pb2.CustomerStateListRequest.SerializeToString,
            customer__state__pb2.CustomerState.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/customer_state.CustomerStateController/Create',
            customer__state__pb2.CustomerState.SerializeToString,
            customer__state__pb2.CustomerState.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/customer_state.CustomerStateController/Retrieve',
            customer__state__pb2.CustomerStateRetrieveRequest.SerializeToString,
            customer__state__pb2.CustomerState.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/customer_state.CustomerStateController/Update',
            customer__state__pb2.CustomerState.SerializeToString,
            customer__state__pb2.CustomerState.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/customer_state.CustomerStateController/Destroy',
            customer__state__pb2.CustomerState.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
