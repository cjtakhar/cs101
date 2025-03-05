-- Set the seed for reproducibility
SET @seed := 7;

-- Select 777 random records from the table and output to a CSV
SELECT *
FROM teachers_salaries_pset4
ORDER BY RAND(@seed)
LIMIT 777
INTO OUTFILE '/Users/kt/Harvard/CS101/pset4/sample.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';