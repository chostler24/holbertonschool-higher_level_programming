-- computes score average of all records in second_table
ALTER TABLE second_table
ADD average FLOAT
SELECT AVG(score) FROM second_table
