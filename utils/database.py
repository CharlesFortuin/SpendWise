import sqlite3

DATABASE = "database/spendwise.db"

def get_connection():
    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection

def initialize_database():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS transactions 
                   (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL,
                      amount REAL NOT NULL,
                      category TEXT NOT NULL,
                      type TEXT NOT NULL,
                      date TEXT NOT NULL
                   )
            """)
    
    connection.commit()
    connection.close()

def add_transaction(title,amount,category,transaction_type,date):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO transactions
        (title,amount,category,type,date)
        VALUES (?,?,?,?,?)
        """, (title,amount,category,transaction_type,date)
        )
    
    connection.commit()
    connection.close()

def get_transactions():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
            SELECT * 
            FROM transactions
            ORDER by date DESC

        """
        )
    
    transactions = cursor.fetchall()

    connection.close()

    return transactions