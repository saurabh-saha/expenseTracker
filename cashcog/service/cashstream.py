
from threading import Thread
from cashcog.util import utils, dbutils

url = 'https://cashcog.xcnt.io/stream'

dbutils.createTable()

t = Thread(target = utils.processPendingTrans, args = [])
t.setDaemon(True)
t.start()

stream_thread = Thread(target = utils.stream_listener, name = "StreamingThread", args = [url])
stream_thread.start()
