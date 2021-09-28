import logging
import math
import smtplib

import tk

from ui.enroll_user import registration_form

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

def create_otp(OTP_p):
    global OTPp
    OTPp = tk.IntVar()
    corpus = "0123456789"
    OTPp = ""
    size = 6
    length = len(corpus)
    for i in range(size):
        from random import random
        OTPp += corpus[math.floor(random() * length)]
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("775singhj@gmail.com", "27April@1993")
    message = OTPp
    s.sendmail("775singhj@gmail.com", "singhj775@outlook.com", message)
    s.quit()
    return registration_form.register(OTP_p)