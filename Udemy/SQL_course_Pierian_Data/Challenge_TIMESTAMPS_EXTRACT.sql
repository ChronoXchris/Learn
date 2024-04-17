/**
Challenge for Timestamps and Extract
**/
--No.1 Challenge
SELECT TO_CHAR(payment_date, 'MONTH')
FROM payment
GROUP BY TO_CHAR(payment_date, 'MONTH');
--No.1 Solution
/**
SELECT
DISTINCT(TO_CHAR(payment_date,'MONTH'))
FROM payment
**/
--No.2 Challenge
SELECT COUNT (*) 
FROM payment
WHERE EXTRACT(dow FROM payment_date)=1



