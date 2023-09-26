# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import game_pb2 as game__pb2


class GameStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.register = channel.unary_unary(
                '/Game/register',
                request_serializer=game__pb2.Soldier.SerializeToString,
                response_deserializer=game__pb2.ServerOutput.FromString,
                )
        self.missile_approach = channel.unary_stream(
                '/Game/missile_approach',
                request_serializer=game__pb2.Empty.SerializeToString,
                response_deserializer=game__pb2.Missile.FromString,
                )
        self.status = channel.unary_unary(
                '/Game/status',
                request_serializer=game__pb2.Request.SerializeToString,
                response_deserializer=game__pb2.Empty.FromString,
                )
        self.sendMissile = channel.unary_unary(
                '/Game/sendMissile',
                request_serializer=game__pb2.Empty.SerializeToString,
                response_deserializer=game__pb2.Empty.FromString,
                )
        self.update_cordinates = channel.unary_unary(
                '/Game/update_cordinates',
                request_serializer=game__pb2.Update.SerializeToString,
                response_deserializer=game__pb2.Empty.FromString,
                )
        self.status_all = channel.unary_unary(
                '/Game/status_all',
                request_serializer=game__pb2.Empty.SerializeToString,
                response_deserializer=game__pb2.Response.FromString,
                )
        self.print_layout = channel.unary_unary(
                '/Game/print_layout',
                request_serializer=game__pb2.Empty.SerializeToString,
                response_deserializer=game__pb2.Response.FromString,
                )
        self.initiaze = channel.unary_unary(
                '/Game/initiaze',
                request_serializer=game__pb2.Empty.SerializeToString,
                response_deserializer=game__pb2.InitialValues.FromString,
                )
        self.game_status = channel.unary_unary(
                '/Game/game_status',
                request_serializer=game__pb2.Empty.SerializeToString,
                response_deserializer=game__pb2.Response.FromString,
                )
        self.is_commander_alive = channel.unary_unary(
                '/Game/is_commander_alive',
                request_serializer=game__pb2.Empty.SerializeToString,
                response_deserializer=game__pb2.Commander_alive_response.FromString,
                )
        self.was_hit = channel.unary_unary(
                '/Game/was_hit',
                request_serializer=game__pb2.wasHit.SerializeToString,
                response_deserializer=game__pb2.wasHit.FromString,
                )


class GameServicer(object):
    """Missing associated documentation comment in .proto file."""

    def register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def missile_approach(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendMissile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_cordinates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def status_all(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def print_layout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def initiaze(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def game_status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def is_commander_alive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def was_hit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GameServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'register': grpc.unary_unary_rpc_method_handler(
                    servicer.register,
                    request_deserializer=game__pb2.Soldier.FromString,
                    response_serializer=game__pb2.ServerOutput.SerializeToString,
            ),
            'missile_approach': grpc.unary_stream_rpc_method_handler(
                    servicer.missile_approach,
                    request_deserializer=game__pb2.Empty.FromString,
                    response_serializer=game__pb2.Missile.SerializeToString,
            ),
            'status': grpc.unary_unary_rpc_method_handler(
                    servicer.status,
                    request_deserializer=game__pb2.Request.FromString,
                    response_serializer=game__pb2.Empty.SerializeToString,
            ),
            'sendMissile': grpc.unary_unary_rpc_method_handler(
                    servicer.sendMissile,
                    request_deserializer=game__pb2.Empty.FromString,
                    response_serializer=game__pb2.Empty.SerializeToString,
            ),
            'update_cordinates': grpc.unary_unary_rpc_method_handler(
                    servicer.update_cordinates,
                    request_deserializer=game__pb2.Update.FromString,
                    response_serializer=game__pb2.Empty.SerializeToString,
            ),
            'status_all': grpc.unary_unary_rpc_method_handler(
                    servicer.status_all,
                    request_deserializer=game__pb2.Empty.FromString,
                    response_serializer=game__pb2.Response.SerializeToString,
            ),
            'print_layout': grpc.unary_unary_rpc_method_handler(
                    servicer.print_layout,
                    request_deserializer=game__pb2.Empty.FromString,
                    response_serializer=game__pb2.Response.SerializeToString,
            ),
            'initiaze': grpc.unary_unary_rpc_method_handler(
                    servicer.initiaze,
                    request_deserializer=game__pb2.Empty.FromString,
                    response_serializer=game__pb2.InitialValues.SerializeToString,
            ),
            'game_status': grpc.unary_unary_rpc_method_handler(
                    servicer.game_status,
                    request_deserializer=game__pb2.Empty.FromString,
                    response_serializer=game__pb2.Response.SerializeToString,
            ),
            'is_commander_alive': grpc.unary_unary_rpc_method_handler(
                    servicer.is_commander_alive,
                    request_deserializer=game__pb2.Empty.FromString,
                    response_serializer=game__pb2.Commander_alive_response.SerializeToString,
            ),
            'was_hit': grpc.unary_unary_rpc_method_handler(
                    servicer.was_hit,
                    request_deserializer=game__pb2.wasHit.FromString,
                    response_serializer=game__pb2.wasHit.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Game', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Game(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Game/register',
            game__pb2.Soldier.SerializeToString,
            game__pb2.ServerOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def missile_approach(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Game/missile_approach',
            game__pb2.Empty.SerializeToString,
            game__pb2.Missile.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Game/status',
            game__pb2.Request.SerializeToString,
            game__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendMissile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Game/sendMissile',
            game__pb2.Empty.SerializeToString,
            game__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update_cordinates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Game/update_cordinates',
            game__pb2.Update.SerializeToString,
            game__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def status_all(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Game/status_all',
            game__pb2.Empty.SerializeToString,
            game__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def print_layout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Game/print_layout',
            game__pb2.Empty.SerializeToString,
            game__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def initiaze(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Game/initiaze',
            game__pb2.Empty.SerializeToString,
            game__pb2.InitialValues.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def game_status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Game/game_status',
            game__pb2.Empty.SerializeToString,
            game__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def is_commander_alive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Game/is_commander_alive',
            game__pb2.Empty.SerializeToString,
            game__pb2.Commander_alive_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def was_hit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Game/was_hit',
            game__pb2.wasHit.SerializeToString,
            game__pb2.wasHit.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
