from sqlalchemy import text

banco = text("USE estagio;")

table1 = text("""CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(100) NOT NULL, 
    description VARCHAR(100) NOT NULL, 
    value FLOAT NOT NULL);
""")

table2 = text("""CREATE TABLE IF NOT EXISTS products_variants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT, 
    model VARCHAR(100) NOT NULL, 
    color VARCHAR(100) NOT NULL,
    size VARCHAR(100) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE);
""")