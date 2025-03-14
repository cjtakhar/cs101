LOAD DATA INFILE '/var/lib/mysql-files/monthly_revenue.csv'
INTO TABLE revenue
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Date, Land_Class, Land_Category, State, County, @FIPS_Code, Offshore_Region, Revenue_Type, Mineral_Lease_Type, Commodity, Product, @Revenue)
SET 
    Date = STR_TO_DATE(@Date, '%m/%d/%Y'),
    FIPS_Code = NULLIF(@FIPS_Code, ''),
    Offshore_Region = NULLIF(Offshore_Region, ''),
    Product = NULLIF(Product, ''),
    Revenue = NULLIF(@Revenue, '');
