from database.database import get_connection


class Payment:

    @staticmethod
    def add_payment(student_id, amount, description):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO payments
            (student_id, amount, description)
            VALUES (?, ?, ?)
        """, (student_id, amount, description))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_payments():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT payments.*,
                   students.full_name
            FROM payments
            INNER JOIN students
            ON payments.student_id = students.id
            ORDER BY payments.date_paid DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get_payment_by_id(payment_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM payments
            WHERE id = ?
        """, (payment_id,))

        payment = cursor.fetchone()

        conn.close()

        return payment

    @staticmethod
    def update_payment(payment_id, amount, description):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE payments
            SET
                amount = ?,
                description = ?
            WHERE id = ?
        """, (amount, description, payment_id))

        conn.commit()
        conn.close()

    @staticmethod
    def delete_payment(payment_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM payments
            WHERE id = ?
        """, (payment_id,))

        conn.commit()
        conn.close()

    @staticmethod
    def total_payments():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT SUM(amount) AS total
            FROM payments
        """)

        result = cursor.fetchone()

        conn.close()

        if result["total"] is None:
            return 0

        return result["total"]

    @staticmethod
    def count_payments():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM payments
        """)

        result = cursor.fetchone()

        conn.close()

        return result["total"]
    
    @staticmethod
    def search_payments(query):
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                  SELECT payments.*,
                        students.full_name
                  FROM payments
                  INNER JOIN students
                  ON payments.student_id = students.id
                  WHERE students.full_name LIKE ?
                  OR payments.description LIKE ?
                  ORDER BY payments.date_paid DESC
            """, (f"%{query}%", f"%{query}%"))

            rows = cursor.fetchall()

            conn.close()

            return [dict(row) for row in rows]
    
    @staticmethod
    def calculate_pending_payments(total_students, total_collected, fee_per_student=300000):
            expected_total = total_students * fee_per_student
            pending = expected_total - total_collected
            return pending if pending > 0 else 0