#!/usr/bin/python
#coding:utf-8

import zmq
import time
import sys
from Queue import Queue
from threading import Thread

def deliveryGuyThread(m_queue, flag):
    while True:
        if m_queue.qsize() > 0:
            msg = m_queue.get()

            # PROCESS PARCEL HERE
            time.sleep(5)
            print 'msg processed'
            print msg

        else:
            time.sleep(1)

recepionist_port = 8965
delivery_guy_port = 8964

msg_queue = Queue()


# START delivery-guy thread
delivery_guy = Thread(target=deliveryGuyThread, args = (msg_queue, 1))
delivery_guy.setDaemon(True)
delivery_guy.start()


recp_context = zmq.Context()
recp_socket = recp_context.socket(zmq.REP)
recp_socket.bind("tcp://*:%d" % recepionist_port)

while True:
    # wait for sender
    message = recp_socket.recv()
    print 'Received request: ', message
    recp_socket.send('welcome to DHL')
    # PUT message into msg_queue
    msg_queue.put('request111')
