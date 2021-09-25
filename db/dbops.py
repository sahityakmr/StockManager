from model.User import User


class DBOperations:
    instance = None

    def __init__(self):
        DBOperations.instance = self

    def getUser(self, username, password):
        return User(username, password)


# singleton pattern
def getInstance():
    if DBOperations.instance is not None:
        return DBOperations.instance
    return DBOperations()
