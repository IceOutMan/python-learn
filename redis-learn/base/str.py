import base_connect as bs

conn = bs.direct_connection()
def init():
    conn.set('new-string-key','meiken ')

def get():
    result = conn.get('new-string-key')
    print(result)

def append():
    result = conn.append('new-string-key','hello ')
    print(result)

def setrange():
    result = conn.setrange('new-string-key',7,"TFFFFFFFFFF")
    print(result)

def getrange():
    result = conn.getrange('new-string-key',7,10)
    print(result)

def setbit():
    conn.delete('anchor-key')
    # conn.setbit('anchor-key',2,1)
    # conn.setbit('anchor-key',7,1)
    conn.setbit('anchor-key',4,1)
    result = conn.get('anchor-key')
    print(result)

if __name__ == '__main__':
    init()
    append()
    setrange()
    getrange()
    get()
    setbit()

