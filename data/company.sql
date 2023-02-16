DROP TABLE IF EXISTS users;
CREATE TABLE users(
  user_id            TEXT,
  user_first_name    TEXT,
  PRIMARY KEY(user_id)
) WITHOUT ROWID;
INSERT INTO users VALUES("1", "A");
INSERT INTO users VALUES("2", "B");
SELECT * FROM users;

DROP TABLE IF EXISTS products;
CREATE TABLE products(
  product_id          TEXT,
  product_name        TEXT,
  product_price       TEXT,
  PRIMARY KEY(product_id)
) WITHOUT ROWID;
INSERT INTO products VALUES("1", "Product A", "10");
INSERT INTO products VALUES("2", "Product B", "20");
SELECT * FROM products;

DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
  order_id            TEXT,
  order_user_fk       TEXT,
  order_product_fk    TEXT,
  PRIMARY KEY(order_id)
) WITHOUT ROWID;
INSERT INTO orders VALUES("1", "1", "1");
INSERT INTO orders VALUES("2", "1", "2");
INSERT INTO orders VALUES("3", "2", "1");
SELECT * FROM orders;

SELECT * FROM users 
JOIN orders
JOIN products
ON users.user_id = orders.order_user_fk
AND products.product_id = orders.order_product_fk
WHERE users.user_id = "2";


