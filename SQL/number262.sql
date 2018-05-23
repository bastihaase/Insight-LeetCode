-- The Trips table holds all taxi trips. Each trip has a unique Id, while Client_Id and Driver_Id are both foreign keys to the Users_Id at the Users table. Status is an ENUM type of (‘completed’, ‘cancelled_by_driver’, ‘cancelled_by_client’).

-- +----+-----------+-----------+---------+--------------------+----------+
-- | Id | Client_Id | Driver_Id | City_Id |        Status      |Request_at|
-- +----+-----------+-----------+---------+--------------------+----------+
-- | 1  |     1     |    10     |    1    |     completed      |2013-10-01|
-- | 2  |     2     |    11     |    1    | cancelled_by_driver|2013-10-01|
-- | 3  |     3     |    12     |    6    |     completed      |2013-10-01|
-- | 4  |     4     |    13     |    6    | cancelled_by_client|2013-10-01|
-- | 5  |     1     |    10     |    1    |     completed      |2013-10-02|
-- | 6  |     2     |    11     |    6    |     completed      |2013-10-02|
-- | 7  |     3     |    12     |    6    |     completed      |2013-10-02|
-- | 8  |     2     |    12     |    12   |     completed      |2013-10-03|
-- | 9  |     3     |    10     |    12   |     completed      |2013-10-03|
-- | 10 |     4     |    13     |    12   | cancelled_by_driver|2013-10-03|
-- +----+-----------+-----------+---------+--------------------+----------+

-- The Users table holds all users. Each user has an unique Users_Id, and Role is an ENUM type of (‘client’, ‘driver’, ‘partner’).

-- +----------+--------+--------+
-- | Users_Id | Banned |  Role  |
-- +----------+--------+--------+
-- |    1     |   No   | client |
-- |    2     |   Yes  | client |
-- |    3     |   No   | client |
-- |    4     |   No   | client |
-- |    10    |   No   | driver |
-- |    11    |   No   | driver |
-- |    12    |   No   | driver |
-- |    13    |   No   | driver |
-- +----------+--------+--------+

-- Write a SQL query to find the cancellation rate of requests made by unbanned users between Oct 1, 2013 and Oct 3, 2013. For the above tables, your SQL query should return the following rows with the cancellation rate being rounded to two decimal places.

-- +------------+-------------------+
-- |     Day    | Cancellation Rate |
-- +------------+-------------------+
-- | 2013-10-01 |       0.33        |
-- | 2013-10-02 |       0.00        |
-- | 2013-10-03 |       0.50        |
-- +------------+-------------------+

SELECT completed.Request_at Day,
    ROUND(COALESCE(1.0 * cancelled.numer / completed.denom, 0),2) "Cancellation Rate"
FROM  (SELECT COUNT(t.id) numer, t.Request_at
        FROM Trips t
        LEFT JOIN Users u
        ON t.Client_Id = u.Users_Id
        LEFT JOIN Users u2
        ON t.Client_Id = u2.Users_Id
        WHERE
        CASE
                WHEN t.Status = "cancelled_by_client" THEN u.Banned = "No"
                WHEN t.Status = "cancelled_by_driver" THEN u2.Banned = "No"
                ELSE FALSE
        END
        GROUP BY t.Request_at) cancelled
RIGHT JOIN  (SELECT COUNT(t.ID) denom, t.Request_at
        FROM Trips t
        LEFT JOIN Users u
        ON t.Client_Id = u.Users_Id
        LEFT JOIN Users u2
        ON t.Client_Id = u2.Users_Id
        WHERE
        CASE
                WHEN t.Status = "cancelled_by_client" THEN u.Banned = "Yes"
                WHEN t.Status = "cancelled_by_driver" THEN u2.Banned = "Yes"
                ELSE TRUE
        END
        GROUP BY t.Request_at) completed
ON cancelled.Request_at = completed.Request_at;


SELECT Trips.Request_at 'Day',
round(sum(if(Trips.Status != 'completed', 1, 0)) / sum(1), 2) 'Cancellation Rate'
FROM Trips JOIN Users ON Trips.Client_Id = Users.Users_Id
WHERE Users.Banned = 'No' AND Trips.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Trips.Request_at