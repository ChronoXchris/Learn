--Challenge No.1
SELECT COUNT(amount) FROM payment
WHERE amount > 5.00;

--Challenge No.2
SELECT COUNT(*) FROM actor
WHERE first_name LIKE 'P%';

--Challenge No.3
SELECT COUNT(DISTINCT(district)) 
FROM address;

--Challenge No.4
SELECT DISTINCT(district) FROM address
ORDER BY district ASC;

--Challenge No.5
SELECT COUNT(*) FROM film
WHERE rating = 'R' 
AND replacement_cost BETWEEN 5 and 15;

--Challenge No.6
SELECT COUNT(*) FROM film
WHERE title LIKE '%Truman%';


