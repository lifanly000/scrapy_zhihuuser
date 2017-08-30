# coding=utf-8

from pymongo import MongoClient


class MongoData:

    HOST = "127.0.0.1"
    PORT = 27017

    def __init__(self):
        conn = MongoClient(self.HOST, self.PORT)
        db = conn.mydb
        self.my_set = db.zhihu_userinfo

    def insertData(self, mylist):
        self.my_set.insert(mylist)

    def loadData(self):
        return self.my_set.find()



