from flask import Flask, render_template
from utils.database import (
                            initialize_database, 
                            add_transaction,
                            get_transactions)

app = Flask(__name__)


@app.route("/")
def home():

    transactions = get_transactions()

    return render_template(
        "index.html",
        app_name="SpendWise",
        transactions=transactions)



if __name__ == "__main__":
    initialize_database()
    """add_transaction("Salary",15000,"Income","Income","2026-07-15")"""
    app.run(debug=True)