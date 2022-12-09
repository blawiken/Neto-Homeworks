-- 1. Количество исполнителей в каждом жанре
SELECT g.name, genre_id, COUNT(artist_id) a_count FROM artist_genre ag
JOIN genre g ON ag.genre_id = g.id
GROUP BY g.name, ag.genre_id
ORDER BY a_count DESC;

-- 2. Количество треков, вошедших в альбомы 2019-2020 годов
SELECT a.name, a.year, COUNT(t.id) track_count FROM album a
JOIN track t ON a.id = t.album_id
WHERE year BETWEEN 2019 AND 2020
GROUP BY a.name, a.year;

-- 3. Средняя продолжительность треков по каждому альбому
SELECT a.name, a.year, AVG(t.duration) FROM album a
JOIN track t ON a.id = t.album_id
GROUP BY a.name, a.year;

-- 4. Все исполнители, которые не выпустили альбомы в 2020 году
SELECT DISTINCT ar.name FROM artist ar
JOIN artist_album aa ON ar.id = aa.artist_id
JOIN album al ON aa.album_id = al.id
WHERE year != 2020;

-- 5. Названия сборников, в которых присутствует конкретный исполнитель
SELECT DISTINCT c.name, c.year FROM collection c
JOIN collection_track ct ON c.id = ct.collection_id
JOIN track t ON t.id = ct.track_id
JOIN album al ON al.id = t.album_id
JOIN artist_album aa ON al.id = aa.album_id
JOIN artist ar ON ar.id = aa.artist_id
WHERE ar.name = 'Lil';

-- 6. Название альбомов, в которых присутствуют исполнители более 1 жанра
SELECT al.name FROM album al
JOIN artist_album aa ON al.id = aa.album_id
JOIN artist ar ON aa.artist_id = ar.id
JOIN artist_genre ag ON ag.artist_id = ar.id
GROUP BY al.name, ar.name
HAVING COUNT(ag.artist_id) > 1;

-- 7. Наименование треков, которые не входят в сборники
SELECT t.name, ct.track_id  FROM track t
FULL JOIN collection_track ct ON t.id = ct.track_id
GROUP BY t.name, ct.track_id
HAVING ct.track_id IS NULL;

-- 8. Исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
SELECT ar.name, MIN(t.duration) FROM track t
JOIN album al ON t.album_id = al.id
JOIN artist_album aa ON al.id = aa.album_id
JOIN artist ar ON aa.artist_id = ar.id
WHERE t.duration = (SELECT MIN(t.duration) FROM track t)
GROUP BY ar.name;

-- 9. Название альбомов, содержащих наименьшее количество треков
SELECT a.name, track_count FROM (SELECT t.album_id, COUNT(t.album_id) track_count FROM track t GROUP BY t.album_id) tt
JOIN album a ON a.id = tt.album_id
GROUP BY a.name, tt.track_count
HAVING track_count = (SELECT MIN(min_count) FROM (SELECT album_id, COUNT(album_id) min_count FROM track GROUP BY album_id) min_count);