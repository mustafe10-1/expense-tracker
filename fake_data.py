import random
import datetime
import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

categories = ["Food", "Transport", "Shopping", "Entertainment", "Bills"]

for _ in range(200):
    amount = round(random.uniform(5, 120), 2)
    category = random.choice(categories)
    description = f"{category} expense"
    date = str(datetime.date(2023, random.randint(1, 12), random.randint(1, 28)))

    cursor.execute(
        "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
        (amount, category, description, date)
    )

conn.commit()
conn.close()

print("Inserted 200 fake expenses.")
