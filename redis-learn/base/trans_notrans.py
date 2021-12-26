import threading
import time
import base_connect as bs


conn = bs.direct_connection()

def notrans():
    print(conn.incr('notrans:'))
    time.sleep(.1)
    conn.incr('notrans:',-1)

def trans():
    pipeline = conn.pipeline()
    pipeline.incr('trans:')
    time.sleep(.1)
    pipeline.incr('trans:',-1)
    print(pipeline.execute()[0])

if __name__ == '__main__':
    for i in range(0,3):
        # threading.Thread(target=notrans).start()
        threading.Thread(target=trans).start()
    time.sleep(5)