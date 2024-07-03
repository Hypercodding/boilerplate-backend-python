from configurations import cur, conn

def create_imageTable():
    try:
        cur.execute("""CREATE TABLE IF NOT EXIST images(
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    filename VARCHAR(255),
                    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )""")
        conn.commit()
        print("table images created")
    except Exception as e:
        print(f"Error creating table: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    create_imageTable()
