import sqlite3


def connect_database():
    global conn, cur

    # will connect to db if exists, or create a new one.
    conn = sqlite3.connect('multi_sql_data.db')

    cur = conn.cursor()


def create_database():
    cur.execute('''DROP TABLE IF EXISTS contacts;''')
    cur.execute('''CREATE TABLE IF NOT EXISTS "contacts" (
            "contact_id"	INTEGER PRIMARY KEY,
            "name"	TEXT NOT NULL,
            "position"	TEXT NOT NULL,
            "password"	TEXT NOT NULL,
            "address_id" INTEGER,
            FOREIGN KEY(address_id) REFERENCES addresses(address_id)
            );''')
    cur.execute('''DROP TABLE IF EXISTS addresses;''')
    cur.execute('''CREATE TABLE IF NOT EXISTS "addresses" (
            "address_id"	INTEGER PRIMARY KEY,
            "street"	TEXT NOT NULL,
            "postal"	TEXT NOT NULL,
            "city"	TEXT NOT NULL
            );''')


def close_database():
    conn.commit()
    conn.close()


if __name__ == '__main__':
    connect_database()
    create_database()
    close_database()
