DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS transactions;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE transactions (
  transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL, 
  transaction_name TEXT NOT NULL,
  transaction_date DATE NOT NULL,
  transaction_category TEXT NOT NULL,
  necessity_index BOOLEAN NOT NULL DEFAULT 0,
  FOREIGN KEY (user_id) REFERENCES user (id)
);
