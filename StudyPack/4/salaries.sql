CREATE TABLE salaries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(255),
    first_name VARCHAR(255),
    county VARCHAR(255),
    district VARCHAR(255),
    school VARCHAR(255),
    primary_job VARCHAR(255),
    fte DECIMAL(5,2),
    salary DECIMAL(10,2),
    certificate VARCHAR(255),
    subcategory VARCHAR(255),
    teaching_route VARCHAR(255),
    highly_qualified TEXT,
    experience_district INT,
    experience_nj INT,
    experience_total INT
);

LOAD DATA INFILE '/Users/kt/Harvard/CS101/PSET/pset4/teachersample.csv'
INTO TABLE salaries
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(last_name, first_name, county, district, school, primary_job, fte, salary, certificate, subcategory, teaching_route, highly_qualified, experience_district, experience_nj, experience_total);
