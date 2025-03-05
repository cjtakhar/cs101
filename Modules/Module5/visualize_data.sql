SELECT 'Temperature', 'Sales' FROM cookies.sales

UNION

(SELECT Temperature, Sales FROM cookies.sales
ORDER BY RAND()
LIMIT 25)

INTO OUTFILE '/Users/kt/Harvard/CS101/Modules/Module5/test100.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';