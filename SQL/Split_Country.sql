-- split the column "Country" to different rows
-- create two more table for ID - country 1:1 mapping
CREATE TABLE "DisneyPlus_Country"
AS
SELECT "ID","Title", unnest(string_to_array("Country", ',')) AS "Country"
FROM "DisneyPlus";

CREATE TABLE "Netflix_Country"
AS
SELECT "n_ID", "Title", unnest(string_to_array("Country", ',')) AS "Country"
FROM "Netflix"