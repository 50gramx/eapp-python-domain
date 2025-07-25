# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ethos.elint.collars import DC499999998_pb2 as ethos_dot_elint_dot_collars_dot_DC499999998__pb2


class DC499999998EPME5000CapabilitiesStub(object):
    """-------------------------------------------------------
    gRPC Service Definition
    -------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LaunchVM = channel.unary_unary(
                '/elint.collars.DC499999998EPME5000Capabilities/LaunchVM',
                request_serializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.LaunchVMRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.LaunchVMResponse.FromString,
                )
        self.GetVMInstance = channel.unary_unary(
                '/elint.collars.DC499999998EPME5000Capabilities/GetVMInstance',
                request_serializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetVMInstanceRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetVMInstanceResponse.FromString,
                )
        self.ListVMInstances = channel.unary_unary(
                '/elint.collars.DC499999998EPME5000Capabilities/ListVMInstances',
                request_serializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.ListVMInstancesRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.ListVMInstancesResponse.FromString,
                )


class DC499999998EPME5000CapabilitiesServicer(object):
    """-------------------------------------------------------
    gRPC Service Definition
    -------------------------------------------------------

    """

    def LaunchVM(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVMInstance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListVMInstances(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DC499999998EPME5000CapabilitiesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LaunchVM': grpc.unary_unary_rpc_method_handler(
                    servicer.LaunchVM,
                    request_deserializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.LaunchVMRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.LaunchVMResponse.SerializeToString,
            ),
            'GetVMInstance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVMInstance,
                    request_deserializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetVMInstanceRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetVMInstanceResponse.SerializeToString,
            ),
            'ListVMInstances': grpc.unary_unary_rpc_method_handler(
                    servicer.ListVMInstances,
                    request_deserializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.ListVMInstancesRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.ListVMInstancesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'elint.collars.DC499999998EPME5000Capabilities', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DC499999998EPME5000Capabilities(object):
    """-------------------------------------------------------
    gRPC Service Definition
    -------------------------------------------------------

    """

    @staticmethod
    def LaunchVM(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.collars.DC499999998EPME5000Capabilities/LaunchVM',
            ethos_dot_elint_dot_collars_dot_DC499999998__pb2.LaunchVMRequest.SerializeToString,
            ethos_dot_elint_dot_collars_dot_DC499999998__pb2.LaunchVMResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVMInstance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.collars.DC499999998EPME5000Capabilities/GetVMInstance',
            ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetVMInstanceRequest.SerializeToString,
            ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetVMInstanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListVMInstances(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.collars.DC499999998EPME5000Capabilities/ListVMInstances',
            ethos_dot_elint_dot_collars_dot_DC499999998__pb2.ListVMInstancesRequest.SerializeToString,
            ethos_dot_elint_dot_collars_dot_DC499999998__pb2.ListVMInstancesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DC499999998EPME5001CapabilitiesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUsageMetrics = channel.unary_unary(
                '/elint.collars.DC499999998EPME5001Capabilities/GetUsageMetrics',
                request_serializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetUsageMetricsRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetUsageMetricsResponse.FromString,
                )


class DC499999998EPME5001CapabilitiesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUsageMetrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DC499999998EPME5001CapabilitiesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUsageMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsageMetrics,
                    request_deserializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetUsageMetricsRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetUsageMetricsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'elint.collars.DC499999998EPME5001Capabilities', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DC499999998EPME5001Capabilities(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUsageMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.collars.DC499999998EPME5001Capabilities/GetUsageMetrics',
            ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetUsageMetricsRequest.SerializeToString,
            ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetUsageMetricsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DC499999998EPME5002CapabilitiesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAlerts = channel.unary_unary(
                '/elint.collars.DC499999998EPME5002Capabilities/GetAlerts',
                request_serializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetAlertsRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetAlertsResponse.FromString,
                )


class DC499999998EPME5002CapabilitiesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAlerts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DC499999998EPME5002CapabilitiesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAlerts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAlerts,
                    request_deserializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetAlertsRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetAlertsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'elint.collars.DC499999998EPME5002Capabilities', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DC499999998EPME5002Capabilities(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAlerts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.collars.DC499999998EPME5002Capabilities/GetAlerts',
            ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetAlertsRequest.SerializeToString,
            ethos_dot_elint_dot_collars_dot_DC499999998__pb2.GetAlertsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
