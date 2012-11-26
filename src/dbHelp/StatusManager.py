'''
Created on 2012-11-25

@author: Kevin Lui
'''
class StatusManager:
    
    userType=None
    loginId=None
    @staticmethod
    def getUserType1():
        return StatusManager.userType
    @staticmethod
    def getLoginId1():
        return StatusManager.loginId
    @staticmethod
    def setUserType1(userType):
        StatusManager.userType = userType
    @staticmethod
    def setLoginId1(loginId):
        StatusManager.loginId = loginId
