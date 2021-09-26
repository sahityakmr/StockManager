USER_FIRST_NAME = "fname"
USER_LAST_NAME = "lname"
USER_ID = "userid"
USER_PASSWORD = "password"

userTableConfig = {
    "tableName": "user",
    "cols": [
        "fname TEXT NOT NULL",
        "lname TEXT NOT NULL",
        "userid varchar(100) PRIMARY KEY NOT NULL",
        "password TEXT NOT NULL",
        "TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"
    ]
}

detailTableConfig = {
    "tableName": "details",
    "cols": [
        "detail_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL",
        "driver_name TEXT NOT NULL",
        "helping_hand TEXT",
        "vehicle TEXT NOT NULL",
        "description TEXT NOT NULL",
        "TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP",
        "bill_no TEXT NOT NULL",
    ]
}

weightTableConfig = {
    "tableName": "weight",
    "cols": [
        "weight_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL",
        "weight TEXT NOT NULL"
    ]
}

partsTableConfig = {
    "tableName": "parts",
    "cols": [
        "part_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL",
        "part TEXT NOT NULL",
        "size TEXT NOT NULL",
        "product_code varchar(100) UNIQUE",
        "TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP",
        "product_price int not null"
    ]
}

productTableConfig = {
    "tableName": "product",
    "cols": [
        "product_name TEXT NOT NULL",
        "product_qty DOUBLE NOT NULL",
        "product_price FLOAT",
        "product_code TEXT NOT NULL",
        "product_size TEXT NOT NULL",
        "bill_number TEXT",
        "TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"
    ]
}

accountTableConfig = {
    "tableName": "account",
    "cols": [
        "id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL",
        "party_name TEXT NOT NULL",
        "bill_number TEXT",
        "TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP",
        "product_price int not null"
    ]
}
