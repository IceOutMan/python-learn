import base_connect as bs

conn = bs.direct_connection()

def sadd():
    result = conn.sadd("set-key",'a','b','c')
    print(result)

def srem():
    result = conn.srem('set-key','a','c')
    print(result)

def scard():
    result = conn.scard('set-key')
    print(result)

def smembers():
    result = conn.smembers('set-key')
    print(result)

def smove():
    result = conn.smove('set-key','set-key2','b')
    print(result)

if __name__ == '__main__':
    sadd()
    srem()
    scard()
    smembers()
    smove()
    print(conn.smembers('set-key2'))