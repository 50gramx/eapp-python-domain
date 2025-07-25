# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ethos.elint.services.product.knowledge.space_knowledge_domain_file import create_space_knowledge_domain_file_pb2 as ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file_dot_create__space__knowledge__domain__file__pb2


class CreateSpaceKnowledgeDomainFileServiceStub(object):
    """Service Definitions
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadSpaceKnowledgeDomainFile = channel.stream_stream(
                '/elint.services.product.knowledge.file.CreateSpaceKnowledgeDomainFileService/UploadSpaceKnowledgeDomainFile',
                request_serializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file_dot_create__space__knowledge__domain__file__pb2.UploadSpaceKnowledgeDomainFileRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file_dot_create__space__knowledge__domain__file__pb2.UploadSpaceKnowledgeDomainFileResponse.FromString,
                )


class CreateSpaceKnowledgeDomainFileServiceServicer(object):
    """Service Definitions
    """

    def UploadSpaceKnowledgeDomainFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CreateSpaceKnowledgeDomainFileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadSpaceKnowledgeDomainFile': grpc.stream_stream_rpc_method_handler(
                    servicer.UploadSpaceKnowledgeDomainFile,
                    request_deserializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file_dot_create__space__knowledge__domain__file__pb2.UploadSpaceKnowledgeDomainFileRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file_dot_create__space__knowledge__domain__file__pb2.UploadSpaceKnowledgeDomainFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'elint.services.product.knowledge.file.CreateSpaceKnowledgeDomainFileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CreateSpaceKnowledgeDomainFileService(object):
    """Service Definitions
    """

    @staticmethod
    def UploadSpaceKnowledgeDomainFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/elint.services.product.knowledge.file.CreateSpaceKnowledgeDomainFileService/UploadSpaceKnowledgeDomainFile',
            ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file_dot_create__space__knowledge__domain__file__pb2.UploadSpaceKnowledgeDomainFileRequest.SerializeToString,
            ethos_dot_elint_dot_services_dot_product_dot_knowledge_dot_space__knowledge__domain__file_dot_create__space__knowledge__domain__file__pb2.UploadSpaceKnowledgeDomainFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
