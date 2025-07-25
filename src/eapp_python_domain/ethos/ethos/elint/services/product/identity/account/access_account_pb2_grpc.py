# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ethos.elint.services.product.identity.account import access_account_pb2 as ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2


class AccessAccountServiceStub(object):
    """------------------------------------
    Service Definitions
    ------------------------------------
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ValidateAccount = channel.unary_unary(
                '/elint.services.product.identity.account.AccessAccountService/ValidateAccount',
                request_serializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ValidateAccountRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ValidateAccountResponse.FromString,
                )
        self.VerifyAccount = channel.unary_unary(
                '/elint.services.product.identity.account.AccessAccountService/VerifyAccount',
                request_serializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.VerifyAccountRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.VerifyAccountResponse.FromString,
                )
        self.ValidateAccountServices = channel.unary_unary(
                '/elint.services.product.identity.account.AccessAccountService/ValidateAccountServices',
                request_serializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.AccountServicesAccessAuthDetails.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ValidateAccountServicesResponse.FromString,
                )
        self.ReAccountAccessToken = channel.unary_unary(
                '/elint.services.product.identity.account.AccessAccountService/ReAccountAccessToken',
                request_serializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ReAccountAccessTokenRequest.SerializeToString,
                response_deserializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ReAccountAccessTokenResponse.FromString,
                )


class AccessAccountServiceServicer(object):
    """------------------------------------
    Service Definitions
    ------------------------------------
    """

    def ValidateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateAccountServices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReAccountAccessToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccessAccountServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ValidateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateAccount,
                    request_deserializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ValidateAccountRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ValidateAccountResponse.SerializeToString,
            ),
            'VerifyAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyAccount,
                    request_deserializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.VerifyAccountRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.VerifyAccountResponse.SerializeToString,
            ),
            'ValidateAccountServices': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateAccountServices,
                    request_deserializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.AccountServicesAccessAuthDetails.FromString,
                    response_serializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ValidateAccountServicesResponse.SerializeToString,
            ),
            'ReAccountAccessToken': grpc.unary_unary_rpc_method_handler(
                    servicer.ReAccountAccessToken,
                    request_deserializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ReAccountAccessTokenRequest.FromString,
                    response_serializer=ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ReAccountAccessTokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'elint.services.product.identity.account.AccessAccountService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccessAccountService(object):
    """------------------------------------
    Service Definitions
    ------------------------------------
    """

    @staticmethod
    def ValidateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.services.product.identity.account.AccessAccountService/ValidateAccount',
            ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ValidateAccountRequest.SerializeToString,
            ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ValidateAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerifyAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.services.product.identity.account.AccessAccountService/VerifyAccount',
            ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.VerifyAccountRequest.SerializeToString,
            ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.VerifyAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidateAccountServices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.services.product.identity.account.AccessAccountService/ValidateAccountServices',
            ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.AccountServicesAccessAuthDetails.SerializeToString,
            ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ValidateAccountServicesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReAccountAccessToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elint.services.product.identity.account.AccessAccountService/ReAccountAccessToken',
            ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ReAccountAccessTokenRequest.SerializeToString,
            ethos_dot_elint_dot_services_dot_product_dot_identity_dot_account_dot_access__account__pb2.ReAccountAccessTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
