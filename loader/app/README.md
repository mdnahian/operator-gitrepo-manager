# Operator Git Repository Loader

### Generate gPRC

```bash
cd ./messages/
python -m grpc_tools.protoc -I ../protobuf --python_out=. --grpc_python_out=. ../protobuf/registry.proto
```