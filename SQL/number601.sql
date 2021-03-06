-- X city built a new stadium, each day many people visit it and the stats are saved as these columns: id, date, people

-- Please write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive).
-- For example, the table stadium:

-- +------+------------+-----------+
-- | id   | date       | people    |
-- +------+------------+-----------+
-- | 1    | 2017-01-01 | 10        |
-- | 2    | 2017-01-02 | 109       |
-- | 3    | 2017-01-03 | 150       |
-- | 4    | 2017-01-04 | 99        |
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-08 | 188       |
-- +------+------------+-----------+

-- For the sample data above, the output is:

-- +------+------------+-----------+
-- | id   | date       | people    |
-- +------+------------+-----------+
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-08 | 188       |
-- +------+------------+-----------+

SELECT s1.* FROM stadium AS s1, stadium AS s2, stadium as s3
WHERE
((s1.id + 1 = s2.id
AND s1.id + 2 = s3.id)
OR
(s1.id - 1 = s2.id
AND s1.id + 1 = s3.id)
OR
(s1.id - 2 = s2.id
AND s1.id - 1 = s3.id)
)
AND s1.people>=100
AND s2.people>=100
AND s3.people>=100

GROUP BY s1.id
