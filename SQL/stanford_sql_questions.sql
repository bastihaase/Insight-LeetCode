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
AND h1.name <= h2.name;

-- Q4
-- Find all students who do not appear in the Likes table (as a student who likes or is liked) and return their names and grades. Sort by grade, then by name within each grade.

SELECT h.name,
       h.grade
FROM Highschooler h
LEFT JOIN Likes l1
ON h.ID = l1.ID1
LEFT JOIN Likes l2
ON h.ID = l2.ID2
WHERE l1.ID1 IS NULL
AND l2.ID1 IS NULL;


-- Q5
-- For every situation where student A likes student B, but we have no information about whom B likes (that is, B does not appear as an ID1 in the Likes table), return A and B's names and grades.

SELECT h1.name,
       h1.grade,
       h2.name,
       h2.grade
FROM Highschooler h1
INNER JOIN Likes l1
ON h1.ID = l1.ID1
LEFT JOIN Likes l2
ON l1.ID2 = l2.ID1
INNER JOIN Highschooler h2
ON h2.ID = l1.ID2
WHERE l2.ID1 IS NULL;


-- Q7
-- For each student A who likes a student B where the two are not friends,
-- find if they have a friend C in common (who can introduce them!).
-- For all such trios, return the name and grade of A, B, and C.

SELECT h1.name,
       h1.grade,
       h2.name,
       h2.grade,
       h3.name,
       h3.grade
FROM Highschooler h1
INNER JOIN Likes l
ON h1.ID = l.ID1
LEFT JOIN Friend f
ON l.ID1 = f.ID1
AND l.ID2 = f.ID2
INNER JOIN Highschooler h2
ON l.ID2 = h2.ID
INNER JOIN Friend f2
ON h1.ID = f2.ID1
INNER JOIN Friend f3
ON h2.ID = f3.ID1
AND f2.ID2 = f3.ID2
INNER JOIN Highschooler h3
ON h3.ID = f2.ID2
WHERE f.ID1 IS NULL;

-- Q9. Find the name and grade of all students who are liked by more than one other student.

CREATE
TEMPORARY
TABLE likecount
AS
(SELECT h1.ID,
       COUNT(*) AS likes
FROM Highschooler h1
INNER JOIN Likes l
ON h1.ID = l.ID2
GROUP BY h1.ID);


SELECT h.name,
       h.grade
FROM Highschooler h
INNER JOIN likecount c
ON h.ID = c.ID
AND c.likes > 1;
