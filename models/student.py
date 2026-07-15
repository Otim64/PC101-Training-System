from database.database import get_connection

class Student:

    @staticmethod
    def add_student(full_name, phone, email, course):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students (full_name, phone, email, course)
        VALUES (?, ?, ?, ?)
        """, (full_name, phone, email, course))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_students():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        conn.close()
        return rows

    @staticmethod
    def get_student_by_id(student_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM students
            WHERE id = ?
        """, (student_id,))

        student = cursor.fetchone()

        conn.close()

        return student
    
    @staticmethod
    def update_student(student_id, full_name, phone, email, course):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE students
            SET
                full_name = ?,
                phone = ?,
                email = ?,
                course = ?
            WHERE id = ?
        """, (full_name, phone, email, course, student_id))

        conn.commit()
        conn.close()

    @staticmethod
    def delete_student(student_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM students
            WHERE id = ?
        """, (student_id,))

        conn.commit()
        conn.close()

    @staticmethod
    def count_students():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM students
        """)

        result = cursor.fetchone()

        conn.close()

        return result["total"]