
import base_connect as bs

# user:12 -> hash
# inventory:12 -> set
# market -> zset
import time

import redis.exceptions


conn = bs.direct_connection()

def list_item(conn, itemId, sellerId, price):
    inventory = "inventory:%s" % sellerId
    item = "%s.%s" % (itemId, sellerId)
    end = time.time() + 5
    pipe = conn.pipeline()
    while time.time() < end:
        try:
            pipe.watch(inventory)
            if not pipe.sismember(inventory, itemId):
                pipe.unwatch()
                return None

            pipe.multi()
            pipe.zadd("market:", item, price)
            pipe.srem(inventory, itemId)
            pipe.execute()
            return True
        except redis.exceptions.WatchError:
            pass
    return False



    print(inventory)
