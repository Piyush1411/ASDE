SELECT d.NAME AS Dept_Name, CONCAT('$', CAST(AVG(s.AMT) AS DECIMAL(10, 2))) AS "Average_Monthly_Salary(USD)"
FROM DEPARTMENTS d, Salaries s, employees e
WHERE d.ID = e.DEPT_ID AND e.ID = s.EMP_ID
GROUP BY d.NAME
ORDER BY "Average_Monthly_Salary(USD)" DESC
LIMIT 3;
