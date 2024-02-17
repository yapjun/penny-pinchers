DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS pots;

CREATE TABLE users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER, 
    transaction_name TEXT NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_category TEXT NOT NULL,
    necessity_index BOOLEAN NOT NULL DEFAULT 0,
--   FOREIGN KEY (user_id) REFERENCES users(id)
    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);

CREATE TABLE pots (
    pot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
)
