DROP TABLE IF EXISTS users;
CREATE TABLE users(
  id            TEXT,
  first_name    TEXT,
  PRIMARY KEY(id)
) WITHOUT ROWID;
INSERT INTO users VALUES("1", "A");
INSERT INTO users VALUES("2", "B");
SELECT * FROM users;

DROP TABLE IF EXISTS products;
CREATE TABLE products(
  id          TEXT,
  name        TEXT,
  price       TEXT,
  PRIMARY KEY(id)
) WITHOUT ROWID;
INSERT INTO products VALUES("1", "Product A", "10");
INSERT INTO products VALUES("2", "Product B", "20");
SELECT * FROM products;

DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
  id            TEXT,
  user_fk       TEXT,
  product_fk    TEXT,
  PRIMARY KEY(id)
) WITHOUT ROWID;
INSERT INTO orders VALUES("1", "1", "1");
INSERT INTO orders VALUES("2", "1", "2");
SELECT * FROM orders;

SELECT * FROM users 
JOIN orders
JOIN products
ON users.id = orders.user_fk
AND products.id = orders.product_fk
WHERE users.id = "1";


