import time, datetime, timedelta
import sqlite3
import os
from flask import Flask, render_template, request, url_for, redirect, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    # conn = get_db_connection()
    # users = conn.execute("SELECT * FROM user").fetchall()
    # conn.close()
    return render_template('profile.html')

# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn

if __name__ == "__main__":
    app.run()


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
        
        cur.execute('DELETE FROM transactions WHERE id = ?', (tid,))

        conn.commit()
        
        conn.close()
        
        return jsonify({'message': 'Transaction deleted!'}), 201
    
    except Exception as e:
        return jsonify({'error': 'str(e)'}), 500
