# app.py
from flask import Flask, request, render_template, send_file
import csv
import os
from datetime import datetime
import random

app = Flask(__name__)

# Path for CSV file inside ab_price_test folder
CSV_FILE = os.path.expanduser("~/ab_price_test/data.csv")

# Create CSV file with headers if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Variant"])


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        variant = request.form.get("variant")

        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Append to CSV
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, variant])

        return "Record saved successfully! <br><a href='/'>Go Back</a>"

    # Randomly assign A or B
    variant = random.choice(["A", "B"])
    return render_template("index.html", variant=variant)


@app.route("/records")
def records():
    """Download the CSV file with logged records"""
    return send_file(CSV_FILE, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)

