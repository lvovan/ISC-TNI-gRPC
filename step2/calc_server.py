from concurrent import futures
from datetime import datetime
import grpc

import calc_pb2
import calc_pb2_grpc

class CalcServicer(calc_pb2_grpc.CalcServicer):

    def Add(self, request, context):
        res = request.a + request.b
        print(f"[{datetime.now()}] Add: a={request.a}, b={request.b} => result={res}")
        return calc_pb2.ArithmeticResponse(result = res)

    def Multiply(self, request, context):
        res = request.a * request.b
        print(f"[{datetime.now()}] Multiply: a={request.a}, b={request.b} => result={res}")
        return calc_pb2.ArithmeticResponse(result = res)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calc_pb2_grpc.add_CalcServicer_to_server(CalcServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()