import os
from dotenv import load_dotenv
load_dotenv()

import mysql.connector
from mysql.connector import Error



def get_db_connection():
    """
    Luo tietokantayhteyden ja varmistaa, että tarvittava taulu on olemassa. Jos yhteyden muodostaminen epäonnistuu, tulostaa virheilmoituksen.

    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database='kuopio_decisions'
        )
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS decisions (
            id VARCHAR(20) PRIMARY KEY, 
            title TEXT, 
            link TEXT, 
            description TEXT, 
            date DATE, 
            is_relevant BOOLEAN, 
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        """)
        connection.commit()
        cursor.close()
        return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def save_agenda(decision: dict):
    """
    Tallentaa päätöksen tietokantaan.
    """
    conn = None
    cursor = None

    try:
        conn = get_db_connection()

        cursor = conn.cursor()
        sql = """
            INSERT INTO decisions (id, title, link, description, date, is_relevant)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                title = VALUES(title),
                link = VALUES(link),
                description = VALUES(description),
                date = VALUES(date),
                is_relevant = VALUES(is_relevant)
            """
        values = (
            decision.get('id'),
            decision.get('title'),
            decision.get('link'),
            decision.get('description'),
            decision.get('date'),
            decision.get('is_relevant')
        )
        cursor.execute(sql, values)
        conn.commit()
        print(f"Päätös tallennettu tietokantaan: {decision.get('title')}")

    except Error as e:
        print(f"Error while inserting into MySQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_decisions(relevant_only: bool = False):
    """
    Hakee päätökset tietokannasta.
    """
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        if relevant_only:
            cursor.execute("SELECT * FROM decisions WHERE is_relevant = TRUE ORDER BY date DESC")
        else:
            cursor.execute("SELECT * FROM decisions ORDER BY date DESC")
        
        decisions = cursor.fetchall()
        return decisions
    except Error as e:
        print(f"Error while fetching from MySQL: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()







if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        print("Yhteys tietokantaan onnistui!")
        decisions = get_decisions(relevant_only=True)
        for decision in decisions:
            print(decision)
    else:
        print("Yhteyden muodostaminen tietokantaan epäonnistui.")
