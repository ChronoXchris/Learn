/**
SELECT column1, column2
FROM table
WHERE conditions;
conditions is a filter 
**/
SELECT COUNT(DISTINCT (title)) FROM film 
WHERE rental_rate > 4 AND replacement_cost >= 19.99
AND rating = 'R';


SELECT COUNT(title) FROM film 
WHERE rating = 'R' OR rating = 'PG-13'

SELECT * FROM film 
WHERE rating != 'R'