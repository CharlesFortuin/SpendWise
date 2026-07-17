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

def insert_transaction(title,amount,category,transaction_type,date):
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

def get_dashboard_data():
    connection = get_connection()
    cursor = connection.cursor()

    #Income    
    cursor.execute(
        """
            SELECT SUM(amount)
            FROM transactions
            WHERE type = 'Income'
        """
        )
    income = cursor.fetchone()[0] or 0

    #Total expenses
    cursor.execute(
        """
            SELECT SUM(amount)
            FROM transactions
            WHERE type = 'Expense'
        """
    )
    expenses = cursor.fetchone()[0] or 0

    #Number of Transactions
    cursor.execute(
        """
            SELECT COUNT(*)
            FROM transactions
        """
    )
    transactions = cursor.fetchone()[0]

    connection.close()

    balance = income - expenses

    return {
        "income" : income,
        "expenses" : expenses,
        "balance" : balance,
        "transactions" : transactions
    }

def remove_transaction(transaction_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
            DELETE FROM transactions
            WHERE id=?
        """,(transaction_id,)
    )

    connection.commit()
    connection.close()

def get_transaction(transaction_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
            SELECT *
            FROM transactions
            WHERE id=?
        """,(transaction_id,)
        )
    
    transaction = cursor.fetchone()

    connection.close()

    return transaction

def get_filtered_transactions(search,selected_type,selected_category):
    connection = get_connection()
    cursor = connection.cursor()

    query="""
            SELECT *
            FROM transactions
            WHERE title LIKE ?
          """
    
    parameters = [f"%{search}%"]

    if selected_type:
        query += " AND type = ?"
        parameters.append(selected_type)
    
    if selected_category:
        query += " AND category = ?"
        parameters.append(selected_category)
    
    query += " ORDER BY date DESC"
    
    cursor.execute(query, parameters)

    transactions = cursor.fetchall()

    connection.close()

    return transactions

def update_transaction(transaction_id,title,amount,category,transaction_type,date):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
            UPDATE transactions
            SET
                title=?,
                amount=?,
                category=?,
                type=?,
                date=?
            WHERE id=?
        """,(title,amount,category,transaction_type,date,transaction_id)
        )
    
    connection.commit()
    connection.close()