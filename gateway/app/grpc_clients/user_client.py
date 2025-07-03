import grpc
from app.proto import user_pb2, user_pb2_grpc

def get_user_by_id(user_id: int):
    with grpc.insecure_channel("user:50051") as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        request = user_pb2.UserIdRequest(id=user_id)
        return stub.GetUserById(request)