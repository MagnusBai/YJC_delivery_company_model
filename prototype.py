from Queue import Queue
from threading import Thread
import time

# process every parcel
def consumerThread(m_queue, flag):
    while True:
        if m_queue.qsize() > 0:
            msg = m_queue.get()
            print msg

        time.sleep(1)

msg_queue = Queue()
msg_queue.put('\n----msg1----')
msg_queue.put('\n----msg2----')
msg_queue.put('\n----msg3----')
msg_queue.put('\n----msg4----')

consumer = Thread(target = consumerThread, args = (msg_queue, 1))
consumer.setDaemon(True)
consumer.start()

for i in range(5, 10):
    # get parcel from sender
    msg_queue.put('\n----msg%d----' % i)

    time.sleep(3)

    print '\n[main_thread]: size of msg_queue is: ', msg_queue.qsize()
