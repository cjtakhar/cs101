-- Set the seed for reproducibility
SET @seed := 7;

-- Select 777 random records from the salaries table and output to a CSV
SELECT *
FROM nj_state_teachers_salaries.salaries
ORDER BY RAND(@seed)
LIMIT 777
INTO OUTFILE '/Users/kt/Harvard/CS101/PSET/pset4/sample.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n';