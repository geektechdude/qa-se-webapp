DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS asset;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE asset (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serial_number TEXT UNIQUE NOT NULL,
    device_model TEXT NOT NULL,
    purchase_date DATE NOT NULL,
    warranty_exp_date DATE NOT NULL,
    assigned_to TEXT NOT NULL,
    retired BOOLEAN,
    retirment_date DATE
);