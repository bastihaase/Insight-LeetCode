-- Stanford SQL questions: https://docs.google.com/document/d/1Di9w-1UL_TLxUu30ekTSi5cIOHTjwa18c6Ww8aJLeZY/edit#

-- Q1 Find all friends of Gabriels

SELECT h1.name
FROM Highschooler h1
INNER JOIN Friend f
ON h1.ID = f.ID1
INNER JOIN Highschooler h2
ON f.ID2 = h2.ID
AND h2.name = "Gabriel";


-- Q2 Find all students who like someone at least two grades below them

SELECT h1.name,
       h1.grade,
       h2.name,
       h2.grade
FROM Highschooler h1
INNER JOIN Likes l
ON h1.ID = l.ID1
INNER JOIN Highschooler h2
ON h2.ID = l.ID2
AND h1.grade - h2.grade > 1;


-- Q3
--    For every pair of students who both like each other,
--    return the name and grade of both students. Include each pair only once,
--    with the two names in alphabetical order.

SELECT h1.name,
       h1.grade,
       h2.name,
       h2.grade
FROM Highschooler h1
INNER JOIN Likes l1
ON h1.ID = l1.ID1
INNER JOIN Likes l2
ON l1.ID1 = l2.ID2
AND l1.ID2 = l2.ID1
INNER JOIN Highschooler h2
ON h2.ID = l2.ID1
AND h1.name < h2.name;
