import grpc
import environ
import os
from django.conf import settings
from service.client.rayan.infrastructure.rayan_pb2_grpc import RecommendationsStub

def client_connection():
    channel = grpc.insecure_channel(
        f"{settings.ENV('RAYAN_URL')}:{settings.ENV('RAYAN_PORT')}",
        options=[
            ('grpc.max_send_message_length', int(settings.ENV("RAYAN_MAX_SEND_SIZE"))),
            ('grpc.max_receive_message_length', int(settings.ENV("RAYAN_MAX_RECIEVE_SIZE"))),
        ],
    )
    return RecommendationsStub(channel)
