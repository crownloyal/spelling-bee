#!/usr/bin/env python3

# import proto
import grpc

# establish grpc channel
channel = grpc.insecure_channel('localhost:7000')
stub = grpc(channel) # inherit from grpc config

word = "random"
response = stub.Attempt(word)
print(response.value)