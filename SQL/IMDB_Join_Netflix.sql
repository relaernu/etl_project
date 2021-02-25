WITH
NetflixMatch (id,n_id,title)
AS
(
	-- 3584 with some duplicates of same PrimaryTitle but different OriginalTitle
	-- 3147 if use OriginalTitle
	SELECT i."ID", n."n_ID", n."Title"
	FROM "IMDB" i JOIN "Netflix" n
	ON i."PrimaryTitle" = n."Title"
	WHERE CAST(i."StartYear" AS INTEGER) = n."ReleaseYear"
),
NotMatch (n_id, title)
AS
(
	-- 1911 PrimaryTitle -- 5495 total
	-- 2313 OriginalTitle -- 5460 total
	SELECT * FROM "Netflix"
	WHERE "n_ID" NOT IN (SELECT n_id FROM NetflixMatch)
),
Duplicate (n_ID)
AS
(
	SELECT n_ID FROM NetflixMatch
	GROUP BY (n_ID)
	HAVING count(1)>1
)
SELECT * FROM NOTMATCH