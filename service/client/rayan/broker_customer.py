from service.client.rayan.infrastructure.rayan_pb2 import MainRequest
from service.client.rayan.connect import client_connection


def customer_list():
    c = client_connection()
    request = MainRequest(name="broker")
    return c.BrokerCustomerListService(request)

def fund_customer_list(service):
    c = client_connection()
    request = MainRequest(name=service)
    return c.FundCustomerListService(request)
