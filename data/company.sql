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
ON user_id = order_user_fk
AND product_id = order_product_fk
WHERE user_id = "1" 
AND product_price < "15";

-- Expand it.. only products which the price is less


SELECT * FROM products WHERE product_name LIKE "%uct%";





DROP TABLE IF EXISTS customers;
CREATE TABLE customers(
  customer_id           TEXT,
  customer_first_name   TEXT,
  customer_total_tweets TEXT,
  PRIMARY KEY(customer_id)
) WITHOUT ROWID;
INSERT INTO customers VALUES("1", "A", 0);
SELECT * FROM customers;

DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
  tweet_id            TEXT,             
  tweet_message       TEXT,       
  tweet_customer_fk   TEXT,       
  PRIMARY KEY(tweet_id)
) WITHOUT ROWID;

INSERT INTO tweets VALUES("10", "Hi", "1");
SELECT * FROM tweets;


-- Trigger 
-- INSERT UPDATE DELETE
-- Time events, when it should happen BEFORE AFTER

DROP TRIGGER IF EXISTS increment_total_tweets;
CREATE TRIGGER increment_total_tweets AFTER INSERT ON tweets
BEGIN
  UPDATE customers
  SET customer_total_tweets = customer_total_tweets + "1"
  WHERE customer_id = NEW.tweet_customer_fk;
END;


