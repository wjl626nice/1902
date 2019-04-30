# hashlib
import hashlib, random


# 获取 md5 加密之后的摘要
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


# 用户类
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

        print(self.salt)


user1 = User('michael', '123456')
user2 = User('bob', 'abc999')
user3 = User('alice', 'alice2008')

# 组织临时数据，用户名为键，用户对象为值，用户对象中 有 username, password, salt
db = {
    'michael': user1,
    'bob': user2,
    'alice': user3
}


def login(username, password):

    user = db[username]

    return user.password == get_md5(password + user.salt)


print(login('michael', '123456'))