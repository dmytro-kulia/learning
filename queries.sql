-- 1. All columns, all rows
SELECT * FROM products;

-- 2. Only names
SELECT name FROM products;

-- 3. Name and price
SELECT name, price FROM products;

-- 4. Only fruit
SELECT * FROM products WHERE category = 'fruit';

-- 5. Price above 2
SELECT * FROM products WHERE price > 2;

-- 6. Price 1.5 or less
SELECT * FROM products WHERE price <= 1.5;

-- 7. Dairy products priced above 1
SELECT * FROM products WHERE category = 'dairy' AND price > 1;

-- 8. Bakery or fruit
SELECT * FROM products WHERE category = 'bakery' OR category = 'fruit';

-- 9. Out of stock
SELECT * FROM products WHERE stock = 0;

-- 10. By price, cheapest first
SELECT * FROM products ORDER BY price;

-- 11. By price, most expensive first
SELECT * FROM products ORDER BY price DESC;

-- 12. Names in alphabetical order
SELECT name FROM products ORDER BY name;

-- 13. Dairy products, most expensive first
SELECT * FROM products WHERE category = 'dairy' ORDER BY price DESC;

-- 14. Three most expensive products
SELECT * FROM products ORDER BY price DESC LIMIT 3;

-- 15. Name and stock, lowest stock first
SELECT name, stock FROM products ORDER BY stock;