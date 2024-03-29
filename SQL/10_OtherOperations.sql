-- Search IMDB Title Duplicate Records
SELECT * FROM "IMDB" i WHERE EXISTS (
	SELECT 1 FROM "IMDB" i2
	WHERE i2."PrimaryTitle" = i."PrimaryTitle" AND i2."ReleaseYear" = i."ReleaseYear"
	AND i2."ID" != i."ID")
ORDER BY "PrimaryTitle";