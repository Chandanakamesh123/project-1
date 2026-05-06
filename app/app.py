from flask import Flask, render_template, request
from src.model import recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        product = request.form["product"]
        budget = request.form.get("budget")

        budget = float(budget) if budget else None
        results = recommend(product, budget)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
