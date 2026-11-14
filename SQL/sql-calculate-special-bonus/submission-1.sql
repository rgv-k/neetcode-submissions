-- Write your query below
SELECT 
    employee_id, 
    CASE 
        WHEN MOD(employee_id, 2) = 1 AND substring(name, 1, 1) <> 'M' THEN salary * 1
        ELSE salary * 0
    END AS bonus
FROM employees ORDER BY employee_id ASC;