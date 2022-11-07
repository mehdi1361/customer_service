import grpc
import environ
import os
from django.conf import settings
from service.client.sms.sms_pb2_grpc import SmsServiceStub

def client_connection():
    channel = grpc.insecure_channel(
        f"{settings.ENV('SMS_SERVICE_URL')}:{settings.ENV('SMS_SERVICE_PORT')}",
        options=[
            ('grpc.max_send_message_length', int(settings.ENV("SMS_SERVICE_MAX_RECIEVE_SIZE"))),
            ('grpc.max_receive_message_length', int(settings.ENV("SMS_SERVICE_MAX_SEND_SIZE"))),
        ],
    )
    return SmsServiceStub(channel)
