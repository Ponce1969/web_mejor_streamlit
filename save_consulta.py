import sqlite3 as sqlite


def open_connection():
    conn = sqlite.connect('my_database.db')
    return conn


def create_database():
    """
    Crea la tabla 'consulta' si no existe en la base de datos.
    """
    try:
        conn = open_connection()
        cursor = conn.cursor()
        cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS consultas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL,
                    asunto TEXT NOT NULL,
                    mensaje TEXT NOT NULL
                )
                """
            )
        conn.commit()
    except sqlite.Error as e:
        print("Error al crear la base de datos:", e)

    finally:
        conn.close()
        

def save_consulta(nombre, email, asunto, mensaje):
    """
    Guarda una consulta en la base de datos.
    """
    try:
        conn = open_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO consultas (nombre, email, asunto, mensaje)
            VALUES (?, ?, ?, ?)
            """,
            (nombre, email, asunto, mensaje),
        )
        conn.commit()
    except sqlite.Error as e:
        print("Error al insertar datos:", e)
    finally:
        conn.close()


        