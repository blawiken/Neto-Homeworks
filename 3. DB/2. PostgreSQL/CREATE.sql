CREATE TABLE IF NOT EXISTS genre (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS artist (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS artist_genre (
	genre_id INTEGER REFERENCES genre(id),
	artist_id INTEGER REFERENCES artist(id),
	CONSTRAINT artist_genre_pk PRIMARY KEY (genre_id, artist_id)
);

CREATE TABLE IF NOT EXISTS album (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE,
	year INTEGER NOT NULL CHECK (year BETWEEN 1900 and 2022)
);

CREATE TABLE IF NOT EXISTS artist_album (
	album_id INTEGER REFERENCES album(id),
	artist_id INTEGER REFERENCES artist(id),
	CONSTRAINT artist_album_pk PRIMARY KEY (album_id, artist_id)
);

CREATE TABLE IF NOT EXISTS track (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	duration INTEGER NOT NULL CHECK (duration BETWEEN 1 and 500),
	album_id INTEGER NOT NULL REFERENCES album(id)
);

CREATE TABLE IF NOT EXISTS collection (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE,
	year INTEGER NOT NULL CHECK (year BETWEEN 1900 and 2022)
);

CREATE TABLE IF NOT EXISTS collection_track (
	track_id INTEGER REFERENCES track(id),
	collection_id INTEGER REFERENCES collection(id),
	CONSTRAINT collection_track_pk PRIMARY KEY (collection_id, track_id)
);