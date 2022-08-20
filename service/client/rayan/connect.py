import grpc
import environ
import os
from django.conf import settings
from service.client.rayan.infrastructure.rayan_pb2_grpc import RecommendationsStub

def load_env():
    env = environ.Env()
    env.read_env(os.path.join(settings.BASE_DIR, '.env'))
    return env

def client_connection():
    env = load_env()
    channel = grpc.insecure_channel(
        f"{env('RAYAN_URL')}:{env('RAYAN_PORT')}",
        options=[
            ('grpc.max_send_message_length', int(env("RAYAN_MAX_SEND_SIZE"))),
            ('grpc.max_receive_message_length', int(env("RAYAN_MAX_RECIEVE_SIZE"))),
        ],
    )
    return RecommendationsStub(channel)
