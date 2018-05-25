-- Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

-- +----+-------+
-- | Id | Score |
-- +----+-------+
-- | 1  | 3.50  |
-- | 2  | 3.65  |
-- | 3  | 4.00  |
-- | 4  | 3.85  |
-- | 5  | 4.00  |
-- | 6  | 3.65  |
-- +----+-------+

-- For example, given the above Scores table, your query should generate the following report (order by highest score):

-- +-------+------+
-- | Score | Rank |
-- +-------+------+
-- | 4.00  | 1    |
-- | 4.00  | 1    |
-- | 3.85  | 2    |
-- | 3.65  | 3    |
-- | 3.65  | 3    |
-- | 3.50  | 4    |
-- +-------+------+

-- DOES NOT WORK WITH MYSQL
SELECT Score,
DENSE_RANK() over(order by score desc) AS Rank
FROM
Scores;

-- MySQL
Select Scores.score as Score, rank.rankid as Rank
from
scores left join
(select @rowid := @rowid + 1 as rankid, temp1.score
from
(select distinct score from scores order by score desc) as temp1,
(select @rowid:=0) as temp2) as rank
on Scores.score = rank.score
order by Rank

-- MySQL

SELECT
Score,
@rank := @rank + (@prev <> (@prev := Score)) Rank
FROM
Scores,
(SELECT @rank := 0, @prev := -1) init
ORDER BY Score desc;

SELECT S.Score, COUNT(S.score)
FROM
(SELECT S.score
FROM Scores s
INNER JOIN Scores s2
ON s.Score >= s2.Score);

SELECT s.Score Score,
r.Rank Rank
FROM
Scores s
INNER JOIN
(
SELECT tmp.Score Score,
COUNT(DISTINCT tmp.other) Rank
FROM
(SELECT S.score Score,
s2.Score other
FROM Scores s
INNER JOIN Scores s2
ON s.Score <= s2.Score) tmp
GROUP BY tmp.Score
) r
ON s.Score = r.Score
ORDER BY s.Score DESC;
