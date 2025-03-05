SET SQL_SAFE_UPDATES = 0;

UPDATE cookies.`cookies sample`
SET Sales_Date = DATE_FORMAT(STR_TO_DATE(Sales_Date, '%c/%e/%Y'), '%Y/%m/%d');
