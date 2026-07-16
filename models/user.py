from database.database import get_connection

class User:

    @staticmethod
    def create_user(username, email, password_hash):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
            """, (username, email, password_hash))

            conn.commit()

        except Exception as e:
            print("CREATE USER ERROR:", e)
            raise

        finally:
            conn.close()

    @staticmethod
    def get_user_by_username(username):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM users WHERE username = ?
        """, (username,))

        user = cursor.fetchone()
        conn.close()

        return user

    @staticmethod
    def get_user_by_id(user_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, 
                       username, email, 
                       role,
                       phone, 
                       image
            FROM users
            WHERE id = ?
        """, (user_id,))

        user = cursor.fetchone()
        conn.close()

        return user
    
    @staticmethod
    def update_user_profile(user_id, username, email, phone):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE users
            SET username = ?,
                email = ?,
                phone = ?
            WHERE id = ?
        """, (username, email, phone, user_id))

        conn.commit()
        conn.close()
    
    @staticmethod
    def update_profile_image(user_id, image):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE users
            SET image = ?
            WHERE id = ?
        """, (image, user_id))

        conn.commit()
        conn.close()