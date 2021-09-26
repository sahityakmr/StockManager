import db.constants as db_const
import db.utils as dbutils

class DBInitializer:
    instance = None

    def __init__(self, connection):
        self.connection = connection
        self.cursor = None
        DBInitializer.instance = self

    def initialize(self, db_name):
        self.cursor = self.connection.cursor(buffered=True)
        dbutils.make_database(self.cursor, db_name)
        self.makeTables(self.cursor)
        self.connection.commit()
        self.cursor.close()

    @staticmethod
    def get_instance(connection):
        if DBInitializer.instance is None:
            DBInitializer(connection)
        return DBInitializer.instance

    def makeTables(self, cursor):
        dbutils.make_table(cursor, db_const.userTableConfig)
        dbutils.make_table(cursor, db_const.detailTableConfig)
        dbutils.make_table(cursor, db_const.weightTableConfig)
        dbutils.make_table(cursor, db_const.partsTableConfig)
        dbutils.make_table(cursor, db_const.productTableConfig)
        dbutils.make_table(cursor, db_const.accountTableConfig)
