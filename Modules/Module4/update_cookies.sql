SET SQL_SAFE_UPDATES = 0;

UPDATE cookies.sales
SET Sales_Date = DATE_FORMAT(STR_TO_DATE(Sales_Date, '%c/%e/%Y'), '%Y/%m/%d');