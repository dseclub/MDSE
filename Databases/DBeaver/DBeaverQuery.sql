create table federal (
f_account_name varchar(255),
f_geo varchar(255),
f_vertical varchar(255),
f_account_id varchar(255),
f_account_number varchar(255),
f_lcan varchar(255)
);

select * from federal

INSERT INTO federal  (f_account_name,f_geo,f_vertical,
f_account_id,f_account_number,f_lcan) VALUES
( 'D', 'NA','FEderal/US only', '123456','123456','123456'),
( 'as', 'NA','FEderal/US only', '323456','323456','')


SELECT *, replace(invoice_market, 'NA', 'FED')
FROM stg_invoice, federal
WHERE stg_invoice.invoice_enduser_cust_num = federal.f_lcan


SELECT *, replace(invoice_market, 'NA', 'FED')
FROM stg_invoice, federal
WHERE stg_invoice.invoice_enduser_cust_num = federal.f_lcan

SELECT * from stg_invoice

select * from federal




create table stg_invoice (
invoice_account_name varchar(255),
invoice_market varchar(255),
invoice_enduser_cust_num varchar(255)
);

SELECT * from stg_invoice

INSERT INTO stg_invoice  (invoice_account_name,invoice_market,invoice_enduser_cust_num) VALUES
( 'Dictionaries', 'NA', '123456'),
( 'BeautifulSoup', 'EMEA', '6589871')

INSERT INTO stg_invoice  (invoice_account_name,invoice_market,invoice_enduser_cust_num) VALUES
( 'Dictionaries', 'NA', 223456),
( 'BeautifulSoup', 'EMEA', 6589871)


COPY SQLite.stg_invoice (invoice_account_name,invoice_market,invoice_enduser_cust_num)
FROM 'C:\Users\Roman\Documents\stginvoice.csv'
DELIMETER ','
CSV;

COPY stg_invoice (invoice_account_name,invoice_market,invoice_enduser_cust_num)
FROM 'C:\Users\Roman\Documents\stginvoice.csv'
DELIMETER ','
CSV HEADER;

--
COPY SQLITE.stg_invoice
FROM 'C:\Users\Roman\Documents\stginvoice.csv'
DELIMETER ','
CSV; 
