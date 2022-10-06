-- lists all cities of CA found in db hbtn_0d_usa
SELECT id, name
FROM cities
WHERE state_id IN (
    SELECT id
    FROM state_id
    WHERE name = "California"
) ORDER BY id ASC;
