--challenge No.1
SELECT staff_id,COUNT(amount) FROM payment
GROUP BY staff_id 
ORDER BY COUNT(amount);
--challenge No.2
SELECT rating,ROUND(AVG(replacement_cost),2) FROM film
GROUP BY rating
ORDER BY ROUND(AVG(replacement_cost),2);
--challenge No.3
SELECT customer_id,SUM(amount) FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC
LIMIT 5 


