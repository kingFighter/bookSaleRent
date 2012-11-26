#!/usr/bin/python

# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
from dbHelp.StatusManager import StatusManager

class BookManager:
    def getBookInfo(self,method,key,searchType):
        idenType=None
        if method == 0:
                idenType = "bookIdentifier";
        if method ==1:
                idenType = "supplierIdentifier";
        if method == 2:
                idenType = "bookName";
        if method == 3:
                idenType = "bookType";
        if method ==4:
                idenType = "year";
        if method ==5:
                idenType = "author";
        
        sql = None
        idenType = 'bookName'
        if searchType:
            pass
        else:
            sql = "SELECT * FROM book WHERE " + idenType + " LIKE \'%"+key+"%\'"+" AND state=0";
        #print(sql)
        cur = DbManager.con.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        DbManager.con.commit()
        if data == None:
            return
        result = []
        for i in data:
            result.append(i)
        
        return result
        
    def vagueBookSearch(self,key):
        v=None
        
        
class UserManager:
    def checkUser(self,userType,name,pwd):
        sql = " SELECT * FROM " + userType + " WHERE name=\'%s\' AND pwd=\'%s\' AND state=0;" % (name,pwd)
       # print(sql)
        cur = DbManager.con.cursor()
        cur.execute(sql)
        data = cur.fetchone()
        DbManager.con.commit()
        if data == None:
            return
        
        
        print(data)
        StatusManager.setLoginId1(data[0])
        if userType[0] == 's':
            StatusManager.setUserType1(1)
        elif userType[0] == 'a':
            StatusManager.setUserType1(2)
        elif userType[0] == 'o':
            StatusManager.setUserType1(3)
        
        return True          




     
class DbManager:
    host='localhost'
    user='root'
    pwd='jdbc'
    db = 'DB'
    con = None
    um = UserManager() 
    @staticmethod
    def getUserManager():
        return DbManager.um
    def __init__(self):
        self.connect()
    def connect(self):
        try:
            DbManager.con = mdb.connect(self.host,self.user, self.pwd, self.db);
            cur = DbManager.con.cursor()
            cur.execute("SELECT VERSION()")
            data = cur.fetchone()
            DbManager.con.commit()
            print( "Database version : %s " % data)
            print("Successful!")
        except mdb.Error as e:
            print("Error %d: %s" % (e.args[0],e.args[1]))
            sys.exit(1)
      
                


if __name__=='__main__':
    Db=DbManager()
    Db.connect()
    bm = BookManager()
    bm.getBookInfo(0,'p', 0)