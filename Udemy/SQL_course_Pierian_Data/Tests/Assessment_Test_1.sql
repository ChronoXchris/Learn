/**
Assessment Test 1
**/
--Challenge No.1
SELECT customer_id, staff_id, SUM(amount) FROM payment
WHERE staff_id != 1
GROUP BY customer_id, staff_id
HAVING SUM(amount) >= 110
ORDER BY customer_id ASC;
--Challenge No.2
SELECT COUNT(title) FROM film
WHERE title LIKE 'J%';
--Challenge No.3
SELECT customer_id, first_name, last_name, address_id FROM customer
WHERE first_name LIKE 'E%' AND address_id < 500 
ORDER BY customer_id DESC
LIMIT  1

