import time, datetime
from datetime import timedelta
import sqlite3
import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
import random

app = Flask(__name__)

tips = [
    "Pause, reflect, and resist the urge to splurge!",
    "Quality over quantity!",
    "Are you sure you need this?... 🤕",
    "Make every purchase count!",
    "Focus on your essential expenses first!",
    "Use our pots to plan out your spendings!",
    "Have you tried the 50/30/20 rule?",
    "Stick to your budget!!",
    "Small splurges add up, think twice before getting that latte!",
    "Shop smart, not hard!",
    "Budgeting is sexy 😏",
    "Cut the subscription creep, cancel unused services!",
    "Budgeting is sexy 😏",
    "Needs vs wants. Prioritize your spendings!"
    "Budgeting is sexy 😏",
]

@app.route("/")
def index():
    # conn = get_db_connection()
    # users = conn.execute("SELECT * FROM user").fetchall()
    # conn.close()
    random_tip = random.choice(tips)
    return render_template('profile.html', tip=random_tip)

@app.route("/profile")
def profile():
    random_tip = random.choice(tips)
    return render_template('profile.html', tip=random_tip)

@app.route("/tracker")
def tracker():
    return render_template('tracker.html')

@app.route('/pots')
def pots():
    return render_template('pots.html')


@app.route('/monthly')
def monthly():
    return render_template('monthly.html')

@app.route('/weekly')
def weekly():
    return render_template('weekly.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route("/add", methods=['POST'])
def add_transaction():
    try:
        data = request.get_json()
        
        name = data['name']
        amount = data['amount']
        date = data['date'] # 'YYYY-MM-DD'
        necessity_index = data['necessity']
        category = data['category']
        
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        
        sql = '''INSERT INTO transactions (name, amount, date, necessity_index, category) 
                VALUES (?, ?, ?, ?, ?)'''
        
        cur.execute(sql, (name, amount, date, necessity_index, category))
        conn.commit()
        
        conn.close()
        
        return jsonify({'message': 'Transaction added!'}), 201
    
    except Exception as e:
        return jsonify({'error': 'str(e)'}), 500
    # data = request

    # with conn:
        
    #     cur.execute("INSERT INTO transactions (name, VALUES ()")

def edit_transation():
    return 0

@app.route("/post", methods=["GET"])
def get_current_week_data():
    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Calculate the start and end dates of the current week
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    # Fetch data for the current week
    query = "SELECT * FROM transactions WHERE transaction_date BETWEEN ? AND ?"
    cursor.execute(query, (start_of_week, end_of_week))
    current_week_data = cursor.fetchall()

    # Close the connection
    conn.close()

    return current_week_data

def get_current_month_data():
    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Fetch data for the current month

    current_month = datetime.now().month
    current_year = datetime.now().year
    query = "SELECT * FROM transactions WHERE strftime('%m', transaction_date) = ? AND strftime('%Y', transaction_date) = ?"
    cursor.execute(query, (str(current_month).zfill(2), str(current_year)))
    current_month_data = cursor.fetchall()

    # Close the connection
    conn.close()

    return current_month_data

@app.route("/delete", methods=["DELETE"])
def delete_transaction():
    try:
        data = request.get_json()
        tid = data['transaction_id']

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute('DELETE FROM transactions WHERE id = ?', (tid))

        conn.commit()

        conn.close()

        return jsonify({'message': 'Transaction deleted!'}), 201

    except Exception as e:
        return jsonify({'error': 'str(e)'}), 500


if __name__ == "__main__":
    app.run(debug=True)

