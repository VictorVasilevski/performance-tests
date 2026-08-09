from grpc import Channel
import grpc.experimental.gevent as grpc_gevent


grpc_gevent.init_gevent()


class GrpcClient:
    def __init__(self, channel: Channel):
        self.channel = channel
