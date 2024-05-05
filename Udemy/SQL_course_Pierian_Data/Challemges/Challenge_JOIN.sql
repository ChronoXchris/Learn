/**
CHallenge JOIN Challenge
**/
--No.1 Challenge
SELECT district, email FROM customer
INNER JOIN address
ON address.address_id = customer.address_id
WHERE district = 'California';

--No.2 Challenge
SELECT title, first_name, last_name FROM actor
LEFT JOIN film_actor
ON film_actor.actor_id = actor.actor_id
LEFT JOIN film
ON film.film_id = film_actor.film_id
WHERE first_name = 'Nick' AND last_name = 'Wahlberg'
ORDER BY title ASC
