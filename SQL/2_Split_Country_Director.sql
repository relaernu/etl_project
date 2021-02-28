-- create the movie-country mapping table by spliting country column array value to rows
DROP TABLE IF EXISTS movie_country;
CREATE TABLE movie_country AS
WITH directors (id, country)
AS
(
    SELECT c.id, d."Country"
    FROM "DisneyPlus" d JOIN NetflixDisney c
    ON d."ID" = c.original_id
    UNION
    SELECT c.id, n."Country"
    FROM "Netflix" n JOIN NetflixDisney c
    ON n."n_ID" = c.original_id
)
SELECT id, TRIM(unnest(string_to_array(country, ','))) AS country
FROM directors ORDER BY ID;

-- create the movie-director mapping table by spliting director column array value to rows
DROP TABLE IF EXISTS movie_director;
CREATE TABLE movie_director AS
WITH directors (id, directors)
AS
(
    SELECT c.id, d."Director"
    FROM "DisneyPlus" d JOIN NetflixDisney c
    ON d."ID" = c.original_id
    UNION
    SELECT c.id, n."Director"
    FROM "Netflix" n JOIN NetflixDisney c
    ON n."n_ID" = c.original_id
)
SELECT id, TRIM(unnest(string_to_array(directors, ','))) AS name
FROM directors ORDER BY ID;