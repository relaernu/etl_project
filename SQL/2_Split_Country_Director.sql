-- split the column "Country" to different rows
-- create two more table for ID - country 1:1 mapping
DROP TABLE IF EXISTS "DisneyPlus_Country";
CREATE TABLE "DisneyPlus_Country"
AS
SELECT "ID", TRIM(unnest(string_to_array("Country", ','))) AS "Country"
FROM "DisneyPlus";

DROP TABLE IF EXISTS "Netflix_Country";
CREATE TABLE "Netflix_Country"
AS
SELECT "n_ID", TRIM(unnest(string_to_array("Country", ','))) AS "Country"
FROM "Netflix";


-- split director column from disney as well
DROP TABLE IF EXISTS "DisneyPlus_Director";
CREATE TABLE "DisneyPlus_Director"
AS
SELECT "ID", TRIM(unnest(string_to_array("Director", ','))) AS "Name"
FROM "DisneyPlus";