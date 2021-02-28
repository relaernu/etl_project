-- create age rated table
DROP TABLE IF EXISTS AgeRated;
CREATE TABLE AgeRated(
	id SERIAL,
	rated varchar(4)
);

-- insert rated values
INSERT INTO agerated (rated) VALUES ('2-6');
INSERT INTO agerated (rated) VALUES ('7+');
INSERT INTO agerated (rated) VALUES ('14+');
INSERT INTO agerated (rated) VALUES ('18+');
INSERT INTO agerated (rated) VALUES ('NR');

-- create union table
DROP TABLE IF EXISTS NetflixDisney;
CREATE TABLE NetflixDisney (
	id SERIAL,
	original_id varchar,
	title varchar,
	release_year INT,
	age_rated INT,
	source varchar(1)
);

WITH Combine(original_id, title, year, agerated, source)
AS
(
	SELECT "ID" AS original_id, "Title" AS title, "ReleaseYear" AS year, "Rated" AS agerated, 'D' AS source
	FROM "DisneyPlus"
	UNION
	SELECT "n_ID" AS original_id, "Title" AS title, "ReleaseYear" AS year, "Rating" AS rated, 'N' AS source
	FROM "Netflix"
),
ChangeRated(original_id, title, year, agerated, source)
AS
(
	SELECT original_id, title, year, 
	         CASE WHEN agerated IN ('TV-Y') THEN '2-6'
			      WHEN agerated IN ('TV-G', 'TV-Y7-FV', 'TV-Y7', 'G') THEN '7+'
			      WHEN agerated IN ('TV-14', 'PG-13', 'TV-PG') THEN '14+'
			      WHEN agerated IN ('TV-MA', 'NC-17', 'R') THEN '18+'
			      ELSE 'NR' END AS rated, source
	FROM Combine
)
INSERT INTO NetFlixDisney(original_id, title, release_year, age_rated, source)
SELECT original_id, title, year, r.id, source
FROM ChangeRated c JOIN agerated r
ON c.agerated = r.rated
ORDER BY title;


-- -- get distinct rated values
-- SELECT distinct rated FROM NetFlixDisney;

-- -- find out what the values means
-- -- after search in google for different rating system, we put that into 4 different levels
-- -- "2-6", "7+", "14+", "18+" and "NR" means unrated

-- UPDATE NetFlixDisney
-- SET Rated = '2-6' WHERE Rated = 'TV-Y';

-- UPDATE NetFlixDisney
-- SET Rated = '7+'
-- WHERE Rated IN ('TV-G', 'TV-Y7-FV', 'TV-Y7', 'G');

-- UPDATE NetFlixDisney
-- SET Rated = '14+'
-- WHERE Rated IN ('TV-14', 'PG-13', 'TV-PG');

-- UPDATE NetFlixDisney
-- SET Rated = '18+'
-- WHERE Rated IN ('TV-MA', 'NC-17', 'R');

-- UPDATE NetFlixDisney
-- SET Rated = 'NR'
-- WHERE Rated NOT IN ('2-6', '7+', '14+', '18+');

-- UPDATE NetFlixDisney
-- SET Rated = 'NR'
-- WHERE Rated is null;