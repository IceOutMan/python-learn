import base_connect as bs

conn = bs.direct_connection()

def rpush():
    conn.rpush('list','item1')
    conn.rpush('list','item2')
    conn.rpush('list2','item3')

def brpoplpush():
    result = conn.brpoplpush('list2','list',2)
    print(result)

def lrange():
    result = conn.lrange('list',0,-1)
    print(result)

if __name__ == '__main__':
    # brpoplpush()
    # rpush()
    lrange()
    result = conn.lindex('list',3)
    print(result)
    lrange()
