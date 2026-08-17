import sqlite3


def get_connection():
    connection = sqlite3.connect("student_analytics.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_reports_table():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        upload_date TEXT NOT NULL,
        total_students INTEGER,
        average_marks REAL,
        highest_marks REAL,
        lowest_marks REAL,
        pass_count INTEGER,
        fail_count INTEGER,
        topper TEXT
    )
    """)

    connection.commit()

    connection.close()


def insert_report(
    filename,
    upload_date,
    total_students,
    average_marks,
    highest_marks,
    lowest_marks,
    pass_count,
    fail_count,
    topper
):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO reports (
        filename,
        upload_date,
        total_students,
        average_marks,
        highest_marks,
        lowest_marks,
        pass_count,
        fail_count,
        topper
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        filename,
        upload_date,
        total_students,
        average_marks,
        highest_marks,
        lowest_marks,
        pass_count,
        fail_count,
        topper
    ))

    connection.commit()

    connection.close()


def get_all_reports():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM reports")

    reports = cursor.fetchall()

    connection.close()

    return reports

def get_report_by_id(report_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute("""
        SELECT * FROM reports
        WHERE id = ?
        """, (report_id,))

        report = cursor.fetchone()

        return report

    except sqlite3.Error as error:

        print("Database error:", error)

        return None

    finally:

        connection.close()

def delete_report(report_id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM reports
    WHERE id = ?
    """, (report_id,))

    connection.commit()

    connection.close()

