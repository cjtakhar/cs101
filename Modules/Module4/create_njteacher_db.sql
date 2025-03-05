-- Create database from loading CSV file
CREATE SCHEMA nj_teachers_salaries;

CREATE TABLE nj_teachers_salaries.teacher (
	id INT AUTO_INCREMENT PRIMARY KEY,
	last_name VARCHAR(255),
	first_name VARCHAR(255),
	county VARCHAR(255),
	district VARCHAR(255),
	school VARCHAR(255),
	primary_job VARCHAR(255),
	fte FLOAT,
	salary INT,
	certificate VARCHAR(255),
	subcategory VARCHAR(255),
	teaching_route VARCHAR(255),
	highly_qualified VARCHAR(255),
	experience_district INT,
	experience_nj INT,
	experience_total INT
);

LOAD DATA INFILE '/Users/kt/Harvard/CS101/PSET/pset3/nj_teachers_salaries_pset3.csv'
INTO TABLE nj_teachers_salaries.teacher
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, last_name, first_name, county, district, school, primary_job,
fte, salary, certificate, subcategory, teaching_route,
highly_qualified, experience_district, experience_nj, experience_total); 
