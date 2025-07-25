# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ethos.elint.collars import DC499999996_pb2 as ethos_dot_elint_dot_collars_dot_DC499999996__pb2


class DC499999996EPME5000CapabilitiesStub(object):
    """-------------------------------------------------------
    gRPC Service Definition
    -------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LaunchNotebook = channel.unary_unary(
                '/elint.collars.DC499999996EPME5000Capabilities/LaunchNotebook',
                request_serializer=ethos_dot_elint_dot_collars_dot_DC499999996__pb2.LaunchNotebookRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_collars_dot_DC499999996__pb2.LaunchNotebookResponse.FromString,
                )


class DC499999996EPME5000CapabilitiesServicer(object):
    """-------------------------------------------------------
    gRPC Service Definition
    -------------------------------------------------------

    """

    def LaunchNotebook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DC499999996EPME5000CapabilitiesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LaunchNotebook': grpc.unary_unary_rpc_method_handler(
                    servicer.LaunchNotebook,
                    request_deserializer=ethos_dot_elint_dot_collars_dot_DC499999996__pb2.LaunchNotebookRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_collars_dot_DC499999996__pb2.LaunchNotebookResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'elint.collars.DC499999996EPME5000Capabilities', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DC499999996EPME5000Capabilities(object):
    """-------------------------------------------------------
    gRPC Service Definition
    -------------------------------------------------------

    """

    @staticmethod
    def LaunchNotebook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.collars.DC499999996EPME5000Capabilities/LaunchNotebook',
            ethos_dot_elint_dot_collars_dot_DC499999996__pb2.LaunchNotebookRequest.SerializeToString,
            ethos_dot_elint_dot_collars_dot_DC499999996__pb2.LaunchNotebookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
