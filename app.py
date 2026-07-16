from flask import (
                   Flask, 
                   render_template, 
                   request, 
                   redirect, 
                   url_for)
from utils.database import (
                            initialize_database, 
                            insert_transaction,
                            get_transactions,
                            get_dashboard_data,
                            remove_transaction)

app = Flask(__name__)


@app.route("/")
def home():

    transactions = get_transactions()
    dashboard = get_dashboard_data()

    return render_template(
        "index.html",
        app_name="SpendWise",
        transactions=transactions,
        dashboard=dashboard)

@app.route("/add", methods=["GET","POST"])
def add_transaction():
    if request.method == "POST":
        title = request.form["title"]
        amount = float(request.form["amount"])
        category = request.form["category"]
        transaction_type = request.form["type"]
        date = request.form["date"]

        insert_transaction(
            title,
            amount,
            category,
            transaction_type,
            date
        )
        
        return redirect(url_for("home"))

    return render_template(
        "add_transaction.html",
        app_name = "SpendWise"
    )

@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    remove_transaction(transaction_id)
    return redirect(url_for("home"))


if __name__ == "__main__":
    initialize_database()
    """add_transaction("Salary",15000,"Income","Income","2026-07-15")"""
    app.run(debug=True)