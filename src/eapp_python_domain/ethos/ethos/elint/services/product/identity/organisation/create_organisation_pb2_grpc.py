# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc



class CreateOrganisationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """


class CreateOrganisationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""


def add_CreateOrganisationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'elint.services.product.identity.organisation.CreateOrganisationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CreateOrganisationService(object):
    """Missing associated documentation comment in .proto file."""
