from concurrent import futures
import logging
import grpc

import core
from messages import registry_pb2_grpc

class Registry(registry_pb2_grpc.RegistryServicer):

    # def ListPackages(self, request, context):
    #     return registry_pb2.Package

    def GetPackage(self, request, context):
        return core.get_package_details()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    registry_pb2_grpc.add_RegistryServicer_to_server(Registry(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()