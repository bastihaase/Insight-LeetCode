-- The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

-- +----+-------+--------+--------------+
-- | Id | Name  | Salary | DepartmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Henry | 80000  | 2            |
-- | 3  | Sam   | 60000  | 2            |
-- | 4  | Max   | 90000  | 1            |
-- +----+-------+--------+--------------+

-- The Department table holds all departments of the company.

-- +----+----------+
-- | Id | Name     |
-- +----+----------+
-- | 1  | IT       |
-- | 2  | Sales    |
-- +----+----------+

-- Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.

-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Max      | 90000  |
-- | Sales      | Henry    | 80000  |
-- +------------+----------+--------+


--window and join
SELECT d.name Department,
e.name Employee,
e.Salary Salary
FROM Employee e
INNER JOIN
(SELECT Name, MAX(Salary) OVER (PARTITION BY DepartmentID) m
FROM Employee) e2
ON e.Salary = e2.m
AND e.name = e2.name
INNER JOIN Department d
ON e.DepartmentId = d.Id;


--window but no join
SELECT Department, Employee, Salary FROM
(
SELECT d.name Department,
e.name Employee,
e.Salary Salary,
RANK() OVER (PARTITION BY DepartmentID ORDER BY Salary DESC) hey
FROM Employee e
INNER JOIN Department d
ON e.DepartmentId = d.Id
) tmp
WHERE hey = 1;
