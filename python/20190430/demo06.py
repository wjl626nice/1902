class DBHandler:

    __instance = None

    def __init__(self):
        self.host = "127.0.0.1"
        self.port = "3306"
        self.username = "Leo"
        self.password = "123456"

    # 使用类的静态方法，私有静态字段实现单例模式
    @staticmethod
    def singleDB():

        if DBHandler.__instance:
            # __instance如果存在直接返回
            return DBHandler.__instance
        else:
            # __instance如果不存在，重新实例化一个新的对象赋值给，__instance，返回
            DBHandler.__instance = DBHandler()
            return DBHandler.__instance

    def connectDB(self):
        print("连接数据库")
        pass

    def createTable(self, tname):
        print("创建表")
        pass

    def insertDB(self, sqlstr):
        print("插入数据")

    def deleteDb(self, sqlstr):
        print("删除数据")

    def modifyDB(self, sqlstr):
        print("更改数据")

    def queryDB(self, sqlstr):
        print("查询数据")


# 获取单例对象，推荐使用
dbh1 = DBHandler.singleDB()
dbh2 = DBHandler.singleDB()

print(dbh1)
print(dbh2)

# 直接通过构造方法创建对象，不推荐使用
dbh3 = DBHandler()
print(dbh3)


