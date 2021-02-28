-- joining netflixdisney and IMDB 
SELECT n.*, i."ID" AS imdb_id, i."AverageRating" AS avg_rating, i."Votes" AS votes
FROM netflixdisney n JOIN "IMDB" i
ON n.title = i."PrimaryTitle" and n.release_year = i."ReleaseYear";

-- get all the movie in NetflixDisney table which not in the imdb table
SELECT * FROM netflixdisney
WHERE id IN (
    SELECT n.id
    FROM netflixdisney n JOIN "IMDB" i
    ON n.title = i."PrimaryTitle" AND n.release_year = i."ReleaseYear"
);

-- searching netflix movies with different filtering
-- by Director 
SELECT n.*, i."ID" AS imdb_id, i."AverageRating" AS avg_rating, i."Votes" AS votes
FROM netflixdisney n JOIN "IMDB" i
ON n.title = i."PrimaryTitle" AND n.release_year = i."ReleaseYear"
WHERE EXISTS (
    SELECT 1 FROM movie_director md
    WHERE md.id = n.id
    AND upper(name) LIKE '%JAMES%'
-- or upper(name) = '<director name>'
)
AND n.source='N';

-- searching disneyplus movie that release in specify region
SELECT n.*, i."ID" AS imdb_id, i."AverageRating" AS avg_rating, i."Votes" AS votes
FROM netflixdisney n JOIN "IMDB" i
ON n.title = i."PrimaryTitle" AND n.release_year = i."ReleaseYear"
WHERE EXISTS (
    SELECT 1 FROM movie_country md
    WHERE md.id = n.id
    AND (upper(country) = 'USA' OR upper(country) = 'UNITED STATE')
    -- country for disney and netflix are in different format
)
AND n.source='D';

-- searching movie with IMDB rating higher than 7
SELECT n.*, i."ID" AS imdb_id, i."AverageRating" AS avg_rating, i."Votes" AS votes
FROM netflixdisney n JOIN "IMDB" i
ON n.title = i."PrimaryTitle" AND n.release_year = i."ReleaseYear"
AND i."AverageRating" > 7