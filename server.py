from concurrent import futures
import grpc
import example_pb2_grpc,example_pb2

class Testing(example_pb2_grpc.TestingServicer):
    def sayTest(self,request,context):
        return example_pb2.HelloReply(message=f"Hello,{request.name}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    example_pb2_grpc.add_TestingServicer_to_server(Testing(),server)

    print("Server listeing on port 50051...")
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()