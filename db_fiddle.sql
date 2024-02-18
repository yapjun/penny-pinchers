INSERT INTO users(username, password) 
    VALUES 
    ("johnny", "johnny"),
    ("kelly2", "kelly"),
    ("kelly", "kelly"),
    ("daphne", "daphne"),
    ("des", "des"),
    ("sanchi", "sanchi");


INSERT INTO transactions(user_id, transaction_id, transaction_name, amount, transaction_date, transaction_category, necessity_index)
    VALUES 
    (1, 1, 'Sainsbury February Groceries', 30, '2023-02-17', 'Groceries', '1'),
    (1, 2, 'cheeky ram', 15, '2023-02-17', 'Entertainment', '1'),
    (1, 3, 'Marketplace Sandwich', 3.20, '2023-02-16', 'Food', '1'),
    (1, 4, 'New cute plant!!', 5, '2023-02-15', 'Misc', '0'),
    (1, 5, 'Bus to Uni', 1.20, '2023-02-15', 'Transport', '1'),
    (1, 6, 'Laptop Sleeve', 15, '2023-02-14', 'Misc', '0'),
    (1, 7, 'Forum coffee', 3, '2023-02-13', 'Drinks', '0');
