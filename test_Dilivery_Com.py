import zmq
import sys

recepionist_port = 8965

sender_context = zmq.Context()
sender_socket = sender_context.socket(zmq.REQ)
sender_socket.connect ("tcp://localhost:%d" % recepionist_port)

sender_socket.send ("Hello11111")
message = sender_socket.recv()
print message