INSERT INTO users(username, password) 
    VALUES 
    ("johnny", "johnny"),
    ("kelly2", "kelly"),
    ("kelly", "kelly"),
    ("daphne", "daphne"),
    ("des", "des"),
    ("sanchi", "sanchi");


INSERT INTO transactions(user_id, transaction_name, transaction_date, transaction_category, necessity_index)
    VALUES 
    (1, 'Sainsbury February Groceries', '2023-02-17', 'Groceries', '1'),
    (1, 'cheeky ram', '2023-02-17', 'Entertainment', '1'),
    (1, 'Marketplace Sandwich', '2023-02-16', 'Food', '1'),
    (1, 'New cute plant!!', '2023-02-15', 'Misc.', '0'),
    (1, 'Bus to Uni', '2023-02-15', 'Transport', '1'),
    (1, 'Laptop Sleeve', '2023-02-14', 'Misc', '0'),
    (1, 'Forum coffee', '2023-02-13', 'Drinks', '0');
