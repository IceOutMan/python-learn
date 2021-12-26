
import base_connect as bs

conn = bs.direct_connection()
def z_init():
    conn.zadd('zset-1',{'a':1,'b':2,'c':3})
    conn.zadd('zset-2',{'b':4,'c':1,'d':0})
    conn.sadd('set-1','a','b')


def z_inter_store():
    #默认使用的聚合函数是SUM
    conn.zinterstore('zset-i',['zset-1','zset-2'])
    result = conn.zrange('zset-i',0,-1,withscores=True)
    print(result)

def z_union_store():
    conn.zunionstore('zset-u',['zset-1','zset-2'],aggregate='min')
    result = conn.zrange('zset-u',0,-1,withscores=True)
    print(result)

def z_union_store_two():
    conn.zunionstore('zset-u',['zset-1','zset-2','set-1'])
    result = conn.zrange('zset-u',0,-1,withscores=True)
    print(result)

if __name__ == '__main__':
    z_init()
    z_inter_store()
    z_union_store()
    z_union_store_two()

