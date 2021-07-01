# Snowflake DDL - Data Definition Language
```
    * CREATE – is used to create the database or its objects (like table, index, function, views, triggers and store procedure).
    * DROP – is used to delete objects from the database.
    * ALTER - is used to alter the structure of the database.
    * TRUNCATE – is used to remove all records from a table, including all spaces allocated for the records are removed.
    * COMMENT – is used to add comments to the data dictionary.
```
## create (alter) virtual warehouse
```

// create virtual warehouse
create warehouse test;           -- By default it creates XS-Extra Small size warehouse

-- Warehouse sizes are similar to T-SHIRT sizes from XS to 4X-LARGE
-- Provide warehouse NAME as it is mandatory
-- Below are optional parameters that CREATE WAREHOUSE statement
/*objectProperties ::=
  WAREHOUSE_SIZE = XSMALL | SMALL | MEDIUM | LARGE | XLARGE | XXLARGE | XXXLARGE | X4LARGE
  MAX_CLUSTER_COUNT = <num>
  MIN_CLUSTER_COUNT = <num>
  SCALING_POLICY = STANDARD | ECONOMY
  AUTO_SUSPEND = <num> | NULL
  AUTO_RESUME = TRUE | FALSE
  INITIALLY_SUSPENDED = TRUE | FALSE
  RESOURCE_MONITOR = <monitor_name>
  COMMENT = '<string_literal>'*/

create warehouse my_wh WAREHOUSE_SIZE = MEDIUM;

show warehouses;

use warehouse compute_wh;
use warehouse test;

```
##  create database, schema, table
```
create database company;

create or replace database company;

show databases like 'c%';

use database demo_db;


create or replace schema employee;
create schema if not exists department;
drop schema if exists department;

show schemas like 'e%';

use schema information_schema;
use schema public;


create table EMPLOYEE.A(id number,
               name varchar(20));

create or replace table B(id number(32,5),
               salary number,
               department varchar(10));


```
##  create view
```
-- a materialized view is a database object that contains the results of a query.

create view myview as
    select *
    from "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF001"."CUSTOMER"
    where c_custkey <= 5;

select * from myview;

```

## drop dw, db, scheama, table, stage, view
```
-- drop   delete objects from the database permenently.

drop table employee.empl_details;
drop schema demo_db.empl;
drop database company;
drop warehouse test;
drop view demo_db.public.myview;
drop stage if exists mystage;
drop file format if exists parquet_format;
```
## TRUNCATE
```
-- remove all records from a table, including all memory spaces allocated for the records are removed

TRUNCATE TABLE DEMO_DB.PUBLIC.A;
TRUNCATE TABLE IF EXISTS DEMO_DB.DEPARTMENT.DEPARTMENT_DETAILS;
```
