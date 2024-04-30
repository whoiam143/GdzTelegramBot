import sqlite3 as sql


def create_bd():
    with sql.connect("results.db") as con:
        cur = con.cursor()

        cur.execute(""" CREATE TABLE IF NOT EXISTS score(
            username  TEXT,   
            text  TEXT);
            """)

        con.commit()


def add_result(username, text):
    with sql.connect("results.db") as bd:
        cr = bd.cursor()

    cr.execute("""INSERT INTO score VALUES (?, ?)""",
               (username, text))

    bd.commit()
