# coding=utf-8

from pymongo import MongoClient


class MongoData:

    HOST = "127.0.0.1"
    PORT = 27017

    def __init__(self):
        self.conn = MongoClient(self.HOST, self.PORT)
        db = self.conn.mydb
        self.my_set = db.zhihu_userinfo

    def insertData(self, mylist):
        self.my_set.insert(mylist)

    def loadData(self):
        return self.my_set.find()

    def close(self):
        if self.conn is not None:
            self.conn.close()


