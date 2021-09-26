import mysql.connector
import tkinter.messagebox as mb

global conn, cursor
    #    conn = sqlite3.connect("pythontut.db")
conn = mysql.connector.connect(host="192.168.1.20", user="root", password="jhalla")
cursor = conn.cursor(buffered=True)
cursor.execute("create database if not exists meena")
cursor.execute("use meena")
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `user` (fname TEXT NOT NULL, lname TEXT NOT NULL, userid varchar(100) PRIMARY KEY NOT NULL, password TEXT NOT NULL, TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)''')
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `details` (detail_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, driver_name TEXT NOT NULL,helping_hand TEXT, vehicle TEXT NOT NULL, description TEXT NOT NULL,TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, bill_no TEXT NOT NULL )")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `weight` (weight_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, weight TEXT NOT NULL)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `category` (admin_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, username TEXT, password TEXT)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, username TEXT, password TEXT)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `parts` (part_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, part TEXT NOT NULL, size TEXT NOT NULL,product_code varchar(100) UNIQUE,TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, product_price int not null)")
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `product` (product_name TEXT NOT NULL, product_qty DOUBLE NOT NULL, product_price FLOAT, product_code TEXT NOT NULL,product_size TEXT NOT NULL, bill_number TEXT,TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `godown1` (product_name TEXT NOT NULL, product_qty DOUBLE NOT NULL, product_price FLOAT, product_code varchar(100) NOT NULL,product_size TEXT NOT NULL, bill_number TEXT,TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `account` (id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, party_name TEXT NOT NULL, bill_number TEXT, TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,product_price int not null)''')
cursor.execute(
    '''create table IF NOT EXISTS `tmp1` select product_name,sum(product_qty) as product_qty,product_code,product_size,product_price from godown1 group by product_code, product_name, product_size''')

cursor.execute('''alter table tmp1 modify product_qty double not null''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `tmp2` LIKE tmp1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `tmp3` LIKE tmp1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `tmp4` LIKE tmp1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `tmp5` LIKE tmp1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `tmp6` LIKE tmp1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `tmp7` LIKE tmp1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `tmp8` LIKE tmp1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `tmp9` LIKE tmp1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou_final1` LIKE tmp1 ''')


cursor.execute(
    "CREATE TABLE IF NOT EXISTS `details` (detail_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, driver_name TEXT NOT NULL,helping_hand TEXT, vehicle TEXT NOT NULL, description TEXT NOT NULL,TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, bill_no TEXT NOT NULL )")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `weight` (weight_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, weight TEXT NOT NULL)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `category` (admin_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, username TEXT, password TEXT)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, username TEXT, password TEXT)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `parts` (part_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, part TEXT NOT NULL, size TEXT NOT NULL)")
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `product` (product_name TEXT NOT NULL, product_qty DOUBLE NOT NULL, product_price FLOAT NOT NULL NOT NULL, product_code TEXT NOT NULL,product_size TEXT NOT NULL, bill_number TEXT,TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `account` (id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, party_name TEXT NOT NULL, bill_number TEXT UNIQUE, TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)''')
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `bill_generator` (id INTEGER primary key AUTO_INCREMENT NOT NULL, number int NOT NULL, TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)")

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou` (party_name text not null,contact_no bigint null,bill_number varchar(255) not null,product_name text not null,product_qty double not null,product_size text not null,godown text, product_weight text not null,TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,product_code varchar(255),product_price float not null,id int not null auto_increment primary key, sac text not null)''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou_final1` (party_name TEXT NOT NULL, contact_no BIGINT,bill_number TEXT NOT NULL,product_name TEXT NOT NULL, product_qty double NOT NULL,product_size TEXT NOT NULL,godown TEXT,product_weight TEXT NOT NULL,TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,product_code VARCHAR(50) NOT NULL,product_price FLOAT NOT NULL)''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `godown2` LIKE godown1 ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `godown3` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `godown4` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `godown5` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `godown6` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `godown7` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `godown8` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `godown9` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `pgodown1` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `pgodown2` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `pgodown3` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `pgodown4` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `pgodown5` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `pgodown6` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `pgodown7` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `pgodown8` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `pgodown9` LIKE godown1 ''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou2` LIKE ou ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou3` LIKE ou ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou4` LIKE ou ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou5` LIKE ou ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou6` LIKE ou ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou7` LIKE ou ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou8` LIKE ou ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou9` LIKE ou ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou_final2` LIKE ou_final1 ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou_final3` LIKE ou_final1 ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou_final4` LIKE ou_final1 ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou_final5` LIKE ou_final1 ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou_final6` LIKE ou_final1 ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou_final7` LIKE ou_final1 ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou_final8` LIKE ou_final1 ''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `ou_final9` LIKE ou_final1 ''')
cursor.execute('''create table IF NOT EXISTS `outsheet`(outsheet varchar(255) not null)''')
cursor.execute("SELECT * FROM `outsheet` where outsheet='ou'")
if cursor.fetchone() is None:
    cursor.execute('''insert into outsheet values('ou'),('ou2'),('ou3'),('ou4'),('ou5'),('ou6'),('ou7'),('ou8'),('ou9')''')

cursor.execute(
    '''create table if not exists user_id (userid TEXT NOT NULL, bill_number int not null, TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)''')
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `temporary_parts` (part_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, part TEXT NOT NULL, size TEXT NOT NULL,product_code varchar(100) UNIQUE,TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, product_price int not null)")

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS `godown` (godown TEXT NOT NULL)''')
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `bill_generator` (id INTEGER primary key AUTO_INCREMENT NOT NULL, number int NOT NULL, TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)")

cursor.execute("SELECT * FROM `godown` where godown='godown1'")
if cursor.fetchone() is None:
    cursor.execute(
        '''insert into godown values('godown1'),('godown2'),('godown3'),('godown4'),('godown5'),('godown6'),('godown7'),('godown8'),('godown9')''')

    conn.commit()
cursor.execute('''create table if not exists pgodown (pgodown text not null)''')
cursor.execute("SELECT * FROM `pgodown` where pgodown='pgodown1'")
if cursor.fetchone() is None:
    cursor.execute(
        '''insert into pgodown values('pgodown1'),('pgodown2'),('pgodown3'),('pgodown4'),('pgodown5'),('pgodown6'),('pgodown7'),('pgodown8'),('pgodown9')''')

conn.commit()
cursor.execute('''alter table bill_generator AUTO_INCREMENT=0''')
cursor.execute("SELECT * FROM `bill_generator` where id=0")
if cursor.fetchone() is None:
    cursor.execute('''insert into bill_generator(id,number)values("0","0")''')

    conn.commit()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS `sac` (id INTEGER primary key AUTO_INCREMENT NOT NULL, sac text not null , product_code text not null, TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)")

conn.commit()
cursor.close()
mb.showinfo('Database meena', "Succesfully Created")