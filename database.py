import sqlite3


def init_db(db_path="info.db"):
    con = sqlite3.connect("info.db")
    cur = con.cursor()

    cur.execute("PRAGMA foreign_keys = ON")

    with open("schema.sql", "r") as f:
        schema = f.read()

    cur.executescript(schema)

    con.commit()
    con.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized")
