SELECT name, YEAR FROM album
WHERE YEAR = 2018;

SELECT name, duration FROM track
ORDER BY duration DESC;

SELECT name, duration FROM track
WHERE duration >= 210;

SELECT name, YEAR FROM collection
WHERE YEAR BETWEEN 2018 AND 2020;

SELECT name FROM artist
WHERE name NOT LIKE '% %';

SELECT name FROM track
WHERE name LIKE '%my%';