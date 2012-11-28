#!/usr/bin/python

# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
from dbHelp.StatusManager import StatusManager
import time
class BuyManager:
    def addBuy(self,cusId,bookId,buyTime,amount):
        pass
    

class   CusManager:
    def delCus(self,cusId):
        sql = "UPDATE customer SET state=1 WHERE cusIdentifier='%s'" % cusId ;
        cur = DbManager.con.cursor()
        cur.execute(sql)
        DbManager.con.commit()
        return True
    
    def addCus(self,cusIden, vipIden,
            cusName, cusSex, phone, email, type):
        sql = "INSERT INTO customer  VALUES('%s','%s','%s',%s,'%s','%s',%s,0)" % (cusIden,vipIden,cusName,cusSex,
                                                                                                     phone,email,type)
                                                                                                 
        print(sql)
        try:
            cur=DbManager.con.cursor()
            cur.execute(sql)
            DbManager.con.commit()
            print("addCus Successful!")
            return True
        except mdb.Error as e:
            return False
            print("Error %d: %s" % (e.args[0],e.args[1]))
            #sys.exit(1)
            
        
    def vagueCusSearch(self,key):
        sql = "SELECT * FROM customer WHERE cusName LIKE '%"+key+"%'"+" AND state=0";
        cur = DbManager.con.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        DbManager.con.commit()
        if data == None:
            return []
        result = []
        for i in data:
            result.append(i)
        return result

class SupplierManager:
    
    def delSupplier(self,bookId):
        sql = "UPDATE supplier SET state=1 WHERE supplierIdentifier='%s'" % bookId ;
        cur = DbManager.con.cursor()
        cur.execute(sql)
        DbManager.con.commit()
        return True
    
    def addSupplier(self,iden,name,phone,email):
        sql = "INSERT INTO supplier  VALUES('%s','%s','%s','%s',0)" % (iden,name,phone,email)
                                                                    
        print(sql)
        try:
            cur=DbManager.con.cursor()
            cur.execute(sql)
            DbManager.con.commit()
            print("addSupplier Successful!")
            return True
        except mdb.Error as e:
            return False
            print("Error %d: %s" % (e.args[0],e.args[1]))
            
            #sys.exit(1)
            

    
    def vagueSupplierSearch(self,key):
        
        sql = "SELECT * FROM supplier WHERE supplierName LIKE '%"+key+"%'"+" AND state=0";
        cur = DbManager.con.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        DbManager.con.commit()
        if data == None:
            return []
        result = []
        for i in data:
            result.append(i)
        return result
        
        v=self.getBookInfo(2, key, False)
        return v
    
    def getAllSupplierInfo(self):
        sql="SELECT * FROM supplier WHERE state=0";
        try:
            cur=DbManager.con.cursor()
            cur.execute(sql)
            data = cur.fetchall()
            DbManager.con.commit()
            if data == None:
                return []
            result = []
            for i in data:
                result.append(i[0])
                DbManager.con.commit()
                
        except mdb.Error as e:
            print("Error %d: %s" % (e.args[0],e.args[1]))
            #sys.exit(1)
        return result
    
class BookManager:
    
    def sell(self,id,sAmount,tAmount,cusId):
        left = int(tAmount)-int(sAmount)
        sql = "UPDATE book SET amount = %s" % left
        cur = DbManager.con.cursor()
        cur.execute(sql)
        buyTime=(time.strftime('%Y%m%d%H%M%S ',time.localtime(time.time())))
        DbManager.by.addBuy(cusId, id, buyTime, sAmount)
        
        
    def showStock(self):
        sql = "SELECT * FROM book WHERE amount<=5 AND state=0";
        cur = DbManager.con.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        DbManager.con.commit()
        if data == None:
            return []
        result = []
        for i in data:
            result.append(i)
        return result
        
    
        
    
    def delBook(self,bookId):
        sql = "UPDATE book SET state=1 WHERE bookIdentifier='%s'" % bookId ;
        cur = DbManager.con.cursor()
        cur.execute(sql)
        DbManager.con.commit()
        return True
        
    
    def addBook(self,bookIden, supplierIden,
            bookName, bookType, year, author, retailPrice, rentPrice, originalPrice, amount):
        sql = "INSERT INTO book  VALUES('%s','%s','%s','%s','%s','%s',%s,%s,%s,%s,%s)" % (bookIden,supplierIden,bookName,bookType,
                                                                                                     year,author,retailPrice,rentPrice,
                                                                                                 originalPrice,amount,0);
        print(sql)
        try:
            cur=DbManager.con.cursor()
            
            cur.execute(sql)
            DbManager.con.commit()
            print("addBook Successful!")
            return True
        except mdb.Error as e:
            return False
            print("Error %d: %s" % (e.args[0],e.args[1]))
            #sys.exit(1)
            

    
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
            return []
        result = []
        for i in data:
            result.append(i)
        
        return result
        
    def vagueBookSearch(self,key):
        v=[]
#        for i in range(6):
#            temp = self.getBookInfo(0, key, False)
#            if len(temp)>0:
#                v+=temp 
        v=self.getBookInfo(2, key, False)
        return v
        
        
class UserManager:
    
    def addUser(self,userType,id,name,pwd):
        if userType[0]=='s':
            sId='SAIdentifier'
        elif userType[0]=='a':
            sId='adIdentifier'
        else:
            sId='operatorIdentifier'    
        sql = "INSERT INTO "+userType+"  VALUES('%s','%s','%s',0)" % (id,name,pwd)
                                                             
        print(sql)
        try:
            cur=DbManager.con.cursor()
            
            cur.execute(sql)
            DbManager.con.commit()
            print("addUser Successful!")
            return True
        except mdb.Error as e:
            return False
            print("Error %d: %s" % (e.args[0],e.args[1]))
    
    
    def delUser(self,type,iden):
        if type[0] == 's':
            idName = 'SAIdentifier'
        elif type[0] == 'a':
            idName = 'adIdentifier'
        else:
            idName = 'operatorIdentifier'
        sql = "UPDATE "+type+" SET state=1 WHERE "+idName+"='%s'" % iden ;
        cur = DbManager.con.cursor()
        cur.execute(sql)
        DbManager.con.commit()
        return True
    
    def vagueUserSearch(self,key):
        userType=['superadmin','administrator','operator']
        result = []
        for i in range(3):
            sql = "SELECT * FROM "+userType[i]+" WHERE name LIKE '%"+key+"%'"+" AND state=0";
            cur = DbManager.con.cursor()
            cur.execute(sql)
            data = cur.fetchall()
            DbManager.con.commit()
            if data == None:
                continue
            
            for j in data:
                j = (userType[i],)+j
                result.append(j)
        return result
        
    
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
    bm = BookManager()
    sm = SupplierManager()
    cm = CusManager()
    by = BuyManager()
    @staticmethod
    def getBuyManager():
        return DbManager.by
    @staticmethod
    def getUserManager():
        return DbManager.um
    @staticmethod
    def getBookManager():
        return DbManager.bm
    @staticmethod
    def getSupplierManager():
        return DbManager.sm
    @staticmethod
    def getCusManager():
        return DbManager.cm
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