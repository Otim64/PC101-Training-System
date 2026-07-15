from database.database import get_connection


class Attendance:

    @staticmethod
    def mark_attendance(student_id, status, date):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO attendance (
                student_id,
                status,
                date
            )
            VALUES (?, ?, ?)
        """, (student_id, status, date))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_attendance():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT attendance.*,
                   students.full_name,
                   students.course
            FROM attendance
            INNER JOIN students
            ON attendance.student_id = students.id
            ORDER BY attendance.date DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get_attendance_by_id(attendance_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM attendance
            WHERE id = ?
        """, (attendance_id,))

        row = cursor.fetchone()

        conn.close()

        return row



    @staticmethod
    def count_attendance():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM attendance
        """)

        result = cursor.fetchone()

        conn.close()

        return result["total"]

    @staticmethod
    def get_attendance_by_date(date):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT attendance.*,
                   students.full_name,
                   students.course
            FROM attendance
            INNER JOIN students
            ON attendance.student_id = students.id
            WHERE attendance.date = ?
        """, (date,))

        rows = cursor.fetchall()

        conn.close()

        return rows