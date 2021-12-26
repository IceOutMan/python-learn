
import redis

#直连
def direct_connection():
    # 普通连接
    conn = redis.Redis(host="localhost", port=6379)
    return conn

#通过连接池连
def connection_pool():
    # 连接池
    pool = redis.ConnectionPool(host="localhost", port=6379, max_connections=1024)
    conn = redis.Redis(connection_pool=pool)
    return conn

if __name__ == '__main__':
    conn = direct_connection()
    value = conn.get("MEIKEN:key")
    print(value)