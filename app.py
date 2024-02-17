import time
from flask import Flask
import sqlite3
import os
from flask import Flask, render_template, request, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func
# from sqlalchemy import Column, ForeignKey


# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#         'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class User(db.Model):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(30), nullable=False)
#     def __repr__(self):
#         return f'<User {self.username}>'
    
# class Transactions(db.Model):
#     __tablename__ = "transactions"
#     transaction_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.ForeignKey("user.id")
#     transaction_name = db.Column(db.String(50), nullable=False)
#     transaction_date = db.Column(db.Date, unique=True, nullable=False)
#     transaction_category = db.Column(db.Integer)
#     necessity_index = db.Column(db.Integer)

#     def __repr__(self):
#         return f'<Transaction: {self.transaction_name}>'

@app.route("/")
def index():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM user").fetchall()
    conn.close()
    # return render_template('index.html', users=users)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

