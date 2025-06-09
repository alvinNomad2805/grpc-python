import grpc
import example_pb2,example_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')

    stub = example_pb2_grpc.TestingStub(channel)

    request = example_pb2.HelloRequest(name='checking message')

    response = stub.sayHello(request)

    print(f"the client received : {response.message}")

if __name__ == '__main__':
    run()

    #testin
    