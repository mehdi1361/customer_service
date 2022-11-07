from service.client.sms.sms_pb2 import SmsSendRequest
from service.client.sms.connect import client_connection


def send_sms(phone_number, verification_code):
    connection = client_connection()
    request = SmsSendRequest(
        phone=[phone_number],
        text=[f"کد فعالسازی سامانه کارگزاری بانک خاورمیانه {verification_code}"]
    )
    return connection.SmsService(request)
