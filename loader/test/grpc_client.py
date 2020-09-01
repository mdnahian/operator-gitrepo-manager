import grpc
from messages import registry_pb2, registry_pb2_grpc 

channel = grpc.insecure_channel('localhost:50051')
package = registry_pb2_grpc.RegistryStub(channel)
package.GetPackage(request=registry_pb2.GetPackageRequest(name='prometheus'))