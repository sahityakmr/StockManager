import logging

logger = logging.getLogger("db_utils")


def insert_query_generator(query_config):
    query = 'CREATE TABLE IF NOT EXISTS `' + query_config["tableName"] + '` (' + ', '.join(query_config["cols"]) + ')'
    logger.debug("Making Insert Query : " + query)
    return query


def make_table(cursor, table_config):
    create_query = insert_query_generator(table_config)
    cursor.execute(create_query)


def make_database(cursor, db_name):
    cursor.execute('create database if not exists ' + db_name)
    cursor.execute('use ' + db_name)
