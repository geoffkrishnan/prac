import sqlite3
import csv
from pathlib import Path
from datetime import date
from supermemo2 import review

DB_PATH = Path(__file__).parent / "info.db"


def connect_to_db():
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA foreign_keys = ON")
    return con


def init_db():
    con = connect_to_db()
    schema_path = Path(__file__).parent / "schema.sql"
    with open(schema_path, "r") as f:
        schema = f.read()

    con.executescript(schema)
    con.commit()
    con.close()


def add_problem(url, name=None, problem_number=None):
    con = connect_to_db()
    cur = con.cursor()

    try:
        cur.execute(
            "INSERT INTO problems (url, name, problem_number) VALUES (?, ?, ?)",
            (url, name, problem_number),
        )
    except sqlite3.IntegrityError:
        print("Duplicate problem")
        con.commit()
        con.close()
        return

    con.commit()
    con.close()
    print(f"Added problem: {url}")


def list_problems():
    con = connect_to_db()
    cur = con.cursor()

    for row in cur.execute("SELECT url, name, problem_number FROM problems"):
        url, name, problem_number = row
        result = [url]
        if name:
            result.append(name)
        if problem_number:
            result.append(str(problem_number))
        print(" | ".join(result))

    con.close()


def review_problems():
    con = connect_to_db()
    cur = con.cursor()

    today_date = date.today().isoformat()
    for row in cur.execute(
        "SELECT url, name, problem_number FROM problems WHERE next_review_date <= ?",
        (today_date,),
    ):
        url, name, problem_number = row
        result = [url]
        if name:
            result.append(name)
        if problem_number:
            result.append(str(problem_number))
        print(" | ".join(result))

    con.close()


def complete_problem(problem_number, quality):
    con = connect_to_db()
    cur = con.cursor()

    cur.execute(
        "SELECT id, easiness, interval, reps FROM problems WHERE problem_number = ?",
        (problem_number,),
    )
    row = cur.fetchone()
    if not row:
        print(f"Problem {problem_number} not found")
        con.close()
        return

    problem_id, easiness, interval, reps = row
    new_data = review(quality, easiness, interval, reps)
    new_easiness = new_data["easiness"]
    new_interval = new_data["interval"]
    new_reps = new_data["repetitions"]
    next_date = new_data["review_datetime"][:10]

    cur.execute(
        "UPDATE problems SET easiness=?, interval=?, reps=?, next_review_date=? WHERE id=?",
        (new_easiness, new_interval, new_reps, next_date, problem_id),
    )

    cur.execute(
        "INSERT INTO reviews(problem_id, quality, easiness, interval, reps, review_datetime) VALUES (?, ?, ?, ?, ?, ?)",
        (
            problem_id,
            quality,
            new_easiness,
            new_interval,
            new_reps,
            date.today().isoformat(),
        ),
    )

    con.commit()
    con.close()
    print(f"Completed problem {problem_number}, Next review: {next_date}")


def bulk_add_problems(filepath):
    con = connect_to_db()
    cur = con.cursor()

    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                cur.execute(
                    "INSERT INTO problems (url, name, problem_number) VALUES (?, ?, ?)",
                    (row["url"], row.get("name"), int(row["problem_number"])),
                )
                print(f"Added: {row['problem_number']} - {row.get('name')}")
            except sqlite3.IntegrityError:
                print(
                    f"Duplicate, can't add: {row['problem_number']} - {row.get('name')}"
                )
    con.commit()
    con.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized")
