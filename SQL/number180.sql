-- Write a SQL query to find all numbers that appear at least three times consecutively.

-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  |  1  |
-- | 2  |  1  |
-- | 3  |  1  |
-- | 4  |  2  |
-- | 5  |  1  |
-- | 6  |  2  |
-- | 7  |  2  |
-- +----+-----+

-- For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+


SELECT DISTINCT(l1.Num)
AS ConsecutiveNums
FROM Logs l1
INNER JOIN Logs l2
ON l1.id = l2.id + 1
AND l1.Num = l2.Num
INNER JOIN Logs l3
ON l2.id = l3.id + 1
AND l2.Num = l3.Num;
