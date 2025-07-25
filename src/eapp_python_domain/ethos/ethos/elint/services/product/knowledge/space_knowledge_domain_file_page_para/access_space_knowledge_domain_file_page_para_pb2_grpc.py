# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ethos.elint.services.product.knowledge.space_knowledge_domain_file_page_para import access_space_knowledge_domain_file_page_para_pb2 as ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2


class AccessSpaceKnowledgeDomainFilePageParaServiceStub(object):
    """Service Definitions
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SpaceKnowledgeDomainFilePageParaAccessToken = channel.unary_unary(
                '/elint.services.product.knowledge.para.AccessSpaceKnowledgeDomainFilePageParaService/SpaceKnowledgeDomainFilePageParaAccessToken',
                request_serializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.SpaceKnowledgeDomainFilePageParaAccessTokenRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.SpaceKnowledgeDomainFilePageParaAccessTokenResponse.FromString,
                )
        self.ValidateSpaceKnowledgeDomainFilePageParaServices = channel.unary_unary(
                '/elint.services.product.knowledge.para.AccessSpaceKnowledgeDomainFilePageParaService/ValidateSpaceKnowledgeDomainFilePageParaServices',
                request_serializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.SpaceKnowledgeDomainFilePageParaServicesAccessAuthDetails.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.ValidateSpaceKnowledgeDomainFilePageParaServicesResponse.FromString,
                )


class AccessSpaceKnowledgeDomainFilePageParaServiceServicer(object):
    """Service Definitions
    """

    def SpaceKnowledgeDomainFilePageParaAccessToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateSpaceKnowledgeDomainFilePageParaServices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccessSpaceKnowledgeDomainFilePageParaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SpaceKnowledgeDomainFilePageParaAccessToken': grpc.unary_unary_rpc_method_handler(
                    servicer.SpaceKnowledgeDomainFilePageParaAccessToken,
                    request_deserializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.SpaceKnowledgeDomainFilePageParaAccessTokenRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.SpaceKnowledgeDomainFilePageParaAccessTokenResponse.SerializeToString,
            ),
            'ValidateSpaceKnowledgeDomainFilePageParaServices': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateSpaceKnowledgeDomainFilePageParaServices,
                    request_deserializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.SpaceKnowledgeDomainFilePageParaServicesAccessAuthDetails.FromString,
                    response_serializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.ValidateSpaceKnowledgeDomainFilePageParaServicesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'elint.services.product.knowledge.para.AccessSpaceKnowledgeDomainFilePageParaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccessSpaceKnowledgeDomainFilePageParaService(object):
    """Service Definitions
    """

    @staticmethod
    def SpaceKnowledgeDomainFilePageParaAccessToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.services.product.knowledge.para.AccessSpaceKnowledgeDomainFilePageParaService/SpaceKnowledgeDomainFilePageParaAccessToken',
            ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.SpaceKnowledgeDomainFilePageParaAccessTokenRequest.SerializeToString,
            ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.SpaceKnowledgeDomainFilePageParaAccessTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidateSpaceKnowledgeDomainFilePageParaServices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.services.product.knowledge.para.AccessSpaceKnowledgeDomainFilePageParaService/ValidateSpaceKnowledgeDomainFilePageParaServices',
            ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.SpaceKnowledgeDomainFilePageParaServicesAccessAuthDetails.SerializeToString,
            ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file__page__para_dot_access__space__knowledge__domain__file__page__para__pb2.ValidateSpaceKnowledgeDomainFilePageParaServicesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
