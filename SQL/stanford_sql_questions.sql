-- Stanford SQL questions: https://docs.google.com/document/d/1Di9w-1UL_TLxUu30ekTSi5cIOHTjwa18c6Ww8aJLeZY/edit#

-- Q!

SELECT h1.name
FROM Highschooler h1
INNER JOIN Friend f
ON h1.ID = f.ID1
INNER JOIN Highschooler h2
ON f.ID2 = h2.ID
AND h2.name = "Gabriel";
