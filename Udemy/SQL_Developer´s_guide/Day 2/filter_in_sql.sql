SELECT name, area FROM cities WHERE area > 4000;

SELECT name, price FROM phones
WHERE units_sold > 5000

SELECT name, manufacturer FROM phones
WHERE manufacturer IN ('Apple','Samsung')

SELECT name,(price*units_sold) AS total_revenue FROM phones
WHERE (price*units_sold) > 1000000

-- Write query here to update the 'units_sold' of the phone with name 'N8' to 8543
UPDATE phones
SET units_sold = 8543
WHERE name = 'N8';
-- Write query here to select all rows and columns of the 'phones' table
SELECT * FROM phones;

-- Write your delete SQL here
DELETE FROM phones
WHERE manufacturer IN ('Samsung');

-- Write query here to select all rows and columns from phones
SELECT * FROM phones;