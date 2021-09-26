from db.dbops import DBOperations

class UserService:
    instance = None

    def __init__(self):
        self.dbOps = DBOperations.getInstance()
        UserService.instance = self

    def getUser(self, username, password):
        return self.dbOps.getUser(username, password)

    @staticmethod
    def getInstance():
        if UserService.instance is None:
            UserService()
        return UserService.instance
