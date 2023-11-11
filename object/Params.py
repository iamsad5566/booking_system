class Param:
    def __init__(self, memberSize:int, month:str, date:str, time:str, name:str, phone:int, email:str, occasion:str="Friends"):
        self.memberSize = memberSize
        self.month = month
        self.date = date
        self.time = time
        self.name = name
        self.phone = phone
        self.email = email
        self.occasion = occasion
    def getMemberSize(self) -> int:
        return self.memberSize
    def getMonth(self) -> str:
        return self.month
    def getDate(self) -> str:
        return self.date
    def getTime(self) -> str:
        return self.time
    def getName(self) -> str:
        return self.name
    def getPhone(self) -> str:
        return self.phone
    def geteMail(self) -> str:    
        return self.email
    def getOccasion(self) -> str:
        return self.occasion