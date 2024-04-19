--Challenge No.1
SELECT customer_id FROM payment
ORDER BY payment_date ASC
LIMIT 10;

--Challenge No.2
SELECT title,length FROM film
ORDER BY length asc
LIMIT 5;

--Challenge Bonus
SELECT COUNT(title) FROM film
WHERE length <= 50

