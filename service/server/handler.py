from service.server.service import BankService, ProvinceService, \
    CityService, CustomerComexVisitorService, CustomerService

from service.server.grpc import province_pb2_grpc, bank_pb2_grpc, \
    city_pb2_grpc, customer_comex_visitor_pb2_grpc, customer_pb2_grpc


def grpc_handlers(server):
    bank_pb2_grpc.add_BaseBankControllerServicer_to_server(
        BankService.as_servicer(),
        server
    )
    province_pb2_grpc.add_BaseProvinceControllerServicer_to_server(
        ProvinceService.as_servicer(),
        server
    )

    city_pb2_grpc.add_BaseCitiesControllerServicer_to_server(
        CityService.as_servicer(),
        server
    )

    customer_comex_visitor_pb2_grpc.add_CustomerComexVisitorControllerServicer_to_server(
        CustomerComexVisitorService.as_servicer(),
        server
    )

    customer_pb2_grpc.add_CustomerControllerServicer_to_server(
        CustomerService.as_servicer(),
        server
    )
