from model.User import User
import mysql.connector as sql
from configs.config_reader import ConfigManager
from db.db_init import DBInitializer
import db.constants as db_const


class DBOperations:
    instance = None

    def __init__(self):
        self.dbInitializer = None
        self.configManager = ConfigManager.get_instance()
        self.connection = self.getConnection()
        self.initializeDB()
        self.cursor = self.connection.cursor(buffered=True)
        DBOperations.instance = self

    def getConnection(self):
        hostname = self.configManager.get_val("application.db.host")
        username = self.configManager.get_val("application.db.user")
        port = self.configManager.get_val("application.db.port")
        password = self.configManager.get_val("application.db.pass")
        conn = sql.connect(host=hostname, user=username, password=password, port=port)
        return conn

    def getUser(self, username, password):
        select_qry = "select * from `user` where userid = '{0}' and password = '{1}'".format(username, password)
        self.cursor.execute(select_qry)
        response = self.cursor.fetchone()
        if response is None:
            return None
        return User(response[2], response[3], response[0], response[1])

    def initializeDB(self):
        self.dbInitializer = DBInitializer.get_instance(self.connection)
        self.dbInitializer.initialize(self.configManager.get_val("application.db.db_name"))

    @staticmethod
    def getInstance():
        if DBOperations.instance is not None:
            return DBOperations.instance
        return DBOperations()
