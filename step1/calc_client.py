from __future__ import print_function

import sys

import grpc

import calc_pb2
import calc_pb2_grpc

def run(x, y):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calc_pb2_grpc.CalcStub(channel)
        myRequest = calc_pb2.AddRequest(a=x, b=y)
        r = stub.Add(myRequest)
        print(f"{x} + {y} = {r.result}")

if __name__ == '__main__':
    run(int(sys.argv[1]), int(sys.argv[2]))