--Challenge No.1
SELECT customer_id,COUNT(payment_id) FROM payment
GROUP BY customer_id
HAVING COUNT(payment_id) >= 40;
--Challenge No.2
SELECT customer_id, staff_id, SUM(amount) FROM payment
WHERE staff_id != 1
GROUP BY customer_id, staff_id
HAVING SUM(amount) >= 100
ORDER BY customer_id ASC

 

