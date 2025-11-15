from flask import render_template
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# --- Database helper ---
def get_db():
    conn = sqlite3.connect("expenses.db")
    return conn

# --- Create table on startup ---
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            description TEXT,
            date TEXT
        );
    """)
    conn.commit()
    conn.close()

# --- ROUTES ---

@app.route("/expenses", methods=["GET"])
def get_expenses():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
        (data["amount"], data["category"], data["description"], data["date"])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Expense added"}), 201

@app.route("/expenses/<int:id>", methods=["PUT"])
def update_expense(id):
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE expenses SET amount=?, category=?, description=?, date=? WHERE id=?",
        (data["amount"], data["category"], data["description"], data["date"], id)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Expense updated"})

@app.route("/expenses/<int:id>", methods=["DELETE"])
def delete_expense(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Expense deleted"})

@app.route("/summary")
def summary():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/total")
def total():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_amount = cursor.fetchone()[0]
    conn.close()
    return jsonify({"total": total_amount})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
