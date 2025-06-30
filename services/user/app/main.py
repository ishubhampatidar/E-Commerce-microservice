## gRPC Server

from concurrent import futures
import grpc
import app.proto.user_pb2_grpc as user_pb2_grpc
import app.proto.user_pb2 as user_pb2
from app.database import session_local, Base, engine
from app import crud

Base.metadata.create_all(bind=engine)

class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUserById(self, request, context):
        db = session_local()
        user = crud.get_user_by_id(db, request.id)
        db.close()
        if user:
            return user_pb2.UserResponse(id=user.id, email=user.email, full_name=user.full_name)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("User not found")
        return user_pb2.UserResponse()
    
    def CreateUser(self, request, context):
        db = session_local()
        user = crud.create_user(db, request.email, request.full_name)
        db.close()
        return user_pb2.UserResponse(id=user.id, email=user.email, full_name=user.full_name)
    
def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    server()