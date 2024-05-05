SELECT(
SUM(CASE WHEN department = 'A' THEN 1 ELSE 0 END)/
SUM(case WHEN department = 'B' THEN 1 ELSE 0 END)	
) AS department_ratio
FROM depts;
----------------------------------------------------------------
DELETE FROM depts
WHERE department = 'B';
----------------------------------------------------------------
--NULLIF
----------------------------------------------------------------
SELECT(
SUM(CASE WHEN department = 'A' THEN 1 ELSE 0 END)/
NULLIF(SUM(case WHEN department = 'B' THEN 1 ELSE 0 END),0)
) AS department_ratio
FROM depts