
from collections import Counter
users = [
    {'id':0,'name':'Hero'},
    {'id': 1, 'name': 'Dunn'},
    {'id': 2, 'name': 'Sue'},
    {'id': 3, 'name': 'Chi'},
    {'id': 4, 'name': 'Thor'},
    {'id': 5, 'name': 'Clive'},
    {'id': 6, 'name': 'Hicks'},
    {'id': 7, 'name': 'Devin'},
    {'id': 8, 'name': 'Kate'},
    {'id': 9, 'name': 'Klein'}
]

friendships = [(0,1),(0,2),
               (1,2),(1,3),
               (2,3),(3,4),(4,5),
               (5,6),(5,7),
               (6,8),(7,8),(8,9)
]


def number_of_friends(user):
    return len(user['friends'])

# 朋友的朋友
def friends_of_friend_ids_bad(user):
    # foaf 是朋友的朋友 的英文缩写
    return [foaf['id']
            for friend in user['friends']
            for foaf in friend['friends']]

def not_the_same(user, other_user):
    return user['id'] != other_user['id']

# user 和 other_user 不是朋友判定
def not_friends(user, other_user):
    ''' 遍历user的朋友，所有的朋友都不是 other_user'''
    return all(not_the_same(friend, other_user)
               for friend in user['friends'])

def friends_of_friend_ids(user):
    return Counter(
        foaf['id']
        for friend in user['friends']
        for foaf in friend['friends']
        if not_the_same(user, foaf) and not_friends(user, foaf) # 朋友的朋友既不是user，不是朋友关系
    )

if __name__ == '__main__':

    for user in users:
        user['friends'] = []

    for i,j in friendships:
        # i - j 互为朋友
        users[i]['friends'].append(users[j]) # 把i加为j的朋友
        users[j]['friends'].append(users[i])  # 把j加为i的朋友


    total_connections = sum(number_of_friends(user) for user in users)
    num_users = len(users)
    avg_connections = total_connections / num_users
    print("avg_connections:",avg_connections )

    # 创建一个列表（user_id, number_of_friends)
    num_friends_by_id = [(user['id'], number_of_friends(user))
                          for user in users]

    # 按照元组中的第二个元素进行排序 - 倒序
    num_friends_by_id = sorted(num_friends_by_id, key=lambda x: x[1], reverse=True)
    print(num_friends_by_id)
    print(friends_of_friend_ids(users[3]))






