-- computes score average of all records in second_table
SELECT AVG(score) FROM second_table
UPDATE second_table
SET average = AVG(score)
