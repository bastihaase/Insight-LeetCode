-- The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.

-- +----+-------+--------+--------------+
-- | Id | Name  | Salary | DepartmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Henry | 80000  | 2            |
-- | 3  | Sam   | 60000  | 2            |
-- | 4  | Max   | 90000  | 1            |
-- | 5  | Janet | 69000  | 1            |
-- | 6  | Randy | 85000  | 1            |
-- +----+-------+--------+--------------+

-- The Department table holds all departments of the company.

-- +----+----------+
-- | Id | Name     |
-- +----+----------+
-- | 1  | IT       |
-- | 2  | Sales    |
-- +----+----------+

-- Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables, your SQL query should return the following rows.

-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Max      | 90000  |
-- | IT         | Randy    | 85000  |
-- | IT         | Joe      | 70000  |
-- | Sales      | Henry    | 80000  |
-- | Sales      | Sam      | 60000  |
-- +------------+----------+--------+

SELECT d.Name Department,
       r.Name Employee,
       r.Salary
FROM
        (SELECT Name,
                DepartmentId,
                Salary,
                DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) rank
         FROM Employee) r
         INNER JOIN Department d
         ON d.Id = r.DepartmentId
WHERE r.rank < 4;


-- No window!

SELECT d.name Department,
e.name Employee,
e.Salary
FROM Employee e
INNER JOIN Employee e2
ON e.DepartmentId = e2.DepartmentId
AND e.Salary <= e2.Salary
INNER JOIN Department d
ON e.DepartmentId = d.Id
GROUP BY e.Id
HAVING COUNT(DISTINCT e2.SALARY) <= 3
ORDER BY d.Name , e.Salary DESC;
