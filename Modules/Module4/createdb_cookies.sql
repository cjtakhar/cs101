-- Create database from loading CSV file

CREATE SCHEMA cookies;
CREATE TABLE cookies.sales
(Sales_Date varchar(10),
Day_of_Week varchar(10),
Salesman varchar(10),
Temperature INT,
Tweets INT,
Price FLOAT,
Sales INT);

LOAD DATA INFILE '/Users/kt/Harvard/CS101/Modules/Module4/Cookies Sample.csv'
INTO TABLE cookies.sales
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Sales_Date, Day_of_Week, Salesman, Temperature, Tweets, Price, Sales)
SET Sales_Date = STR_TO_DATE(@Sales_Date, '%m/%d/%Y');