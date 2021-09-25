import db.dbops

dbOps = db.dbops.getInstance()


class UserService:
    instance = None

    def __init__(self):
        UserService.instance = self

    def getUser(self, username, password):
        return dbOps.getUser(username, password)

