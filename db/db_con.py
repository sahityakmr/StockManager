import mysql.connector
from configs.config_reader import ConfigManager


def db_connect():
    config = ConfigManager()
    host = config.get_val("application.db.host")
    user = config.get_val("application.db.user")
    password = config.get_val("application.db.password")
    db_name = config.get_val("application.db.db_name")

    conn = mysql.connector.connect(host=host, user=user, password=password)
    cursor = conn.cursor(buffered=True)
    cursor.execute("create database if not exists ", db_name)
    cursor.execute("use meena")
