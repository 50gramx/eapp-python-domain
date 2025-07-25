# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ethos.elint.services.product.product.space_product import create_space_product_pb2 as ethos_dot_elint_dot_services_dot_product_dot_product_dot_space__product_dot_create__space__product__pb2


class CreateSpaceProductServiceStub(object):
    """Service Definitions
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateAccountSpaceProduct = channel.unary_unary(
                '/elint.services.product.product.space.CreateSpaceProductService/CreateAccountSpaceProduct',
                request_serializer=ethos_dot_elint_dot_services_dot_product_dot_product_dot_space__product_dot_create__space__product__pb2.CreateAccountSpaceProductRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_services_dot_product_dot_product_dot_space__product_dot_create__space__product__pb2.CreateAccountSpaceProductResponse.FromString,
                )


class CreateSpaceProductServiceServicer(object):
    """Service Definitions
    """

    def CreateAccountSpaceProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CreateSpaceProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateAccountSpaceProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAccountSpaceProduct,
                    request_deserializer=ethos_dot_elint_dot_services_dot_product_dot_product_dot_space__product_dot_create__space__product__pb2.CreateAccountSpaceProductRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_services_dot_product_dot_product_dot_space__product_dot_create__space__product__pb2.CreateAccountSpaceProductResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'elint.services.product.product.space.CreateSpaceProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CreateSpaceProductService(object):
    """Service Definitions
    """

    @staticmethod
    def CreateAccountSpaceProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.services.product.product.space.CreateSpaceProductService/CreateAccountSpaceProduct',
            ethos_dot_elint_dot_services_dot_product_dot_product_dot_space__product_dot_create__space__product__pb2.CreateAccountSpaceProductRequest.SerializeToString,
            ethos_dot_elint_dot_services_dot_product_dot_product_dot_space__product_dot_create__space__product__pb2.CreateAccountSpaceProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
