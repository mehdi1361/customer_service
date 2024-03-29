# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from service.client.sms import sms_pb2 as sms__pb2


class SmsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SmsService = channel.unary_unary(
                '/SmsService/SmsService',
                request_serializer=sms__pb2.SmsSendRequest.SerializeToString,
                response_deserializer=sms__pb2.SmsMagfaServiceResponse.FromString,
                )
        self.SmsDbService = channel.unary_unary(
                '/SmsService/SmsDbService',
                request_serializer=sms__pb2.SmsRequest.SerializeToString,
                response_deserializer=sms__pb2.SmsDbServiceResponse.FromString,
                )
        self.SmsStatusService = channel.unary_unary(
                '/SmsService/SmsStatusService',
                request_serializer=sms__pb2.SmsStatusRequest.SerializeToString,
                response_deserializer=sms__pb2.SmsMagfaStatusServiceResponse.FromString,
                )


class SmsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SmsService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SmsDbService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SmsStatusService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SmsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SmsService': grpc.unary_unary_rpc_method_handler(
                    servicer.SmsService,
                    request_deserializer=sms__pb2.SmsSendRequest.FromString,
                    response_serializer=sms__pb2.SmsMagfaServiceResponse.SerializeToString,
            ),
            'SmsDbService': grpc.unary_unary_rpc_method_handler(
                    servicer.SmsDbService,
                    request_deserializer=sms__pb2.SmsRequest.FromString,
                    response_serializer=sms__pb2.SmsDbServiceResponse.SerializeToString,
            ),
            'SmsStatusService': grpc.unary_unary_rpc_method_handler(
                    servicer.SmsStatusService,
                    request_deserializer=sms__pb2.SmsStatusRequest.FromString,
                    response_serializer=sms__pb2.SmsMagfaStatusServiceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SmsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SmsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SmsService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmsService/SmsService',
            sms__pb2.SmsSendRequest.SerializeToString,
            sms__pb2.SmsMagfaServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SmsDbService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmsService/SmsDbService',
            sms__pb2.SmsRequest.SerializeToString,
            sms__pb2.SmsDbServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SmsStatusService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SmsService/SmsStatusService',
            sms__pb2.SmsStatusRequest.SerializeToString,
            sms__pb2.SmsMagfaStatusServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
