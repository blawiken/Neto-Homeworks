INSERT INTO genre(name)
VALUES
	('Hip pop'),
	('Rock'),
	('Country'),
	('Funk'),
	('Jazz');

INSERT INTO artist(name)
VALUES
	('Morgan Wallen'),
	('Lil Baby'),
	('Harry Styles'),
	('Bad Bunny'),
	('Stray Kids'),
	('The Weeknd'),
	('Luke Combs'),
	('Taylor Swift');
	
INSERT INTO artist_genre(genre_id, artist_id)
VALUES
	(1, 1),
	(2, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(5, 6),
	(3, 7),
	(4, 8);
	
INSERT INTO album(name, year)
VALUES
	('II', 1991),
	('Lilu', 1997),
	('Presenting the Fabulous Ronettes', 1964),
	('Here, My Dear', 1978),
	('Nick of Time', 2018),
	('Fine Line', 2019),
	('Heart Like a Wheel', 1975),
	('Back to Mono', 1991);

INSERT INTO artist_album(album_id, artist_id)
VALUES
	(1, 1),
	(1, 2),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8);
	
INSERT INTO track(name, duration, album_id)
VALUES
	('Stronger', 120, 1),
	('Baby Love', 147, 2),
	('Pancho and Lefty', 22, 3),
	('Truth Hurts', 78, 4),
	('Without You', 321, 5),
	('You’re So Vain', 221, 1),
	('Time After Time', 114, 3),
	('Where Is My Mind?', 222, 4),
	('So What', 111, 5),
	('Welcome to the Jungle', 41, 5),
	('Old Town Road', 60, 2),
	('Cannonball', 70, 3),
	('House of Balloons', 80, 1),
	('Cranes in the Sky', 90, 1),
	('Collapse', 114, 2);
	
INSERT INTO collection(name, year)
VALUES
	('Reggae', 2000),
	('Disco', 2018),
	('Classic', 2019),
	('Blues', 2020),
	('New-age', 1987),
	('Ska', 1977),
	('Traditional', 2001),
	('Independent', 1995);
	
INSERT INTO collection_track(track_id, collection_id)
VALUES
	(1, 1),
	(2, 1),
	(1, 2),
	(3, 3),
	(4, 3);