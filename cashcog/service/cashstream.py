from threading import Thread
from cashcog.util import utils, dbutils

url = 'https://cashcog.xcnt.io/stream'

# Create tables
if dbutils.createTable():  # Assuming `createTable` returns True if successful
    print("Tables created successfully. Starting threads...")

    # Start thread for processing pending transactions
    t = Thread(target=utils.processPendingTrans, args=[])
    t.setDaemon(True)
    t.start()

    # Start thread for stream listener
    stream_thread = Thread(target=utils.stream_listener, name="StreamingThread", args=[url])
    stream_thread.start()
else:
    print("Failed to create tables. Threads will not be started.")
