SELECT * FROM customers;
SELECT * FROM customers ORDER BY companyname ASC;
SELECT * FROM customers ORDER BY companyname DESC;

SELECT * FROM products;
-- Aggregate functions
-- Select the most expensive product
SELECT MAX(unitprice) FROM products;
-- ALIAS the MAX(unitprice)
SELECT MAX(unitprice) AS most_expensive_product FROM products;
-- Select the cheapest product
SELECT MIN(unitprice) FROM products;
-- ALIAS the 
SELECT MIN(unitprice) AS least_expensive_product FROM products;
-- Select the average price from all products
SELECT AVG(unitprice) FROM products;
-- Give me the total number of products in the table
SELECT COUNT(*) FROM products;
-- ALIAS
SELECT COUNT(*) AS total_products FROM products;

-- Pagination
SELECT * FROM products LIMIT 0, 5;
-- Get 5 products, ordered by cheapeat to highest
SELECT * FROM products ORDER BY unitprice ASC LIMIT 0, 5;
 -- LIKE with wildcard
 SELECT * FROM customers WHERE contactname LIKE "mar%";
 SELECT * FROM customers WHERE contactname LIKE "%er";
 SELECT * FROM customers WHERE contactname LIKE "%g w%";

-- Tweet elon + message with the word elon + users with elon
-- FULL TEXT SEARCH

-- JOIN
SELECT * FROM customers;
SELECT * FROM orders;

SELECT * FROM orders 
JOIN customers
ON orders.customerid = customers.customerid
WHERE customers.customerid = "VINET" LIMIT 0,2;

-- Create a command that gives all the orders AND PRODUCTS
-- FROM the user the customerid VINET









