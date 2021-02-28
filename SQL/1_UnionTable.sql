-- create union table
DROP TABLE IF EXISTS NetflixDisney;
CREATE TABLE NetFlixDisney (
	id SERIAL,
	title varchar,
	director varchar,
	rated varchar(10),
	country varchar,
	year integer,
	source varchar(1)
);

WITH Combine(title, director, rated, country, year, source)
AS
(
	SELECT "Title" AS title, "Director" AS director, "Rated" AS rated, "Country" AS country, "Year" AS year, 'D' AS source
	FROM "DisneyPlus"
	UNION
	SELECT "Title" AS title, "Director" AS director, "Rating" AS rated, "Country" AS country, "ReleaseYear" AS year, 'N' AS source
	FROM "Netflix"
)
INSERT INTO NetFlixDisney(title, director, rated, country, year, source)
SELECT * FROM Combine ORDER BY title;

-- get distinct rated values
SELECT distinct rated FROM NetFlixDisney;

-- find out what the values means
-- after search in google for different rating system, we put that into 4 different levels
-- "2-6", "7+", "14+", "18+" and "NR" means unrated

UPDATE NetFlixDisney
SET Rated = '2-6' WHERE Rated = 'TV-Y';

UPDATE NetFlixDisney
SET Rated = '7+'
WHERE Rated IN ('TV-G', 'TV-Y7-FV', 'TV-Y7', 'G');

UPDATE NetFlixDisney
SET Rated = '14+'
WHERE Rated IN ('TV-14', 'PG-13', 'TV-PG');

UPDATE NetFlixDisney
SET Rated = '18+'
WHERE Rated IN ('TV-MA', 'NC-17', 'R');

UPDATE NetFlixDisney
SET Rated = 'NR'
WHERE Rated NOT IN ('2-6', '7+', '14+', '18+');

UPDATE NetFlixDisney
SET Rated = 'NR'
WHERE Rated is null;