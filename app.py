import time
from flask import Flask
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
        date = data['date']
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

def delete_transaction():
    return 0
