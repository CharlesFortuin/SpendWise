from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        app_name="SpendWise",
        subtitle="Track your expenses like a professional",
        version="Version 1.0")



if __name__ == "__main__":
    app.run(debug=True)