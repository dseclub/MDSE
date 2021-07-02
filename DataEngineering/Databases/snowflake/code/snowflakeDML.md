# Snowflake DML(INSERT/DELETE/UPDATE)   
```
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
```
## select  
```
SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."CALL_CENTER" limit 10;

```
##  WHERE with AND OR Operator
```
SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."CALL_CENTER"
    WHERE CC_CALL_cENTER_SK < 5 AND CC_CLASS = 'large';

SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."CALL_CENTER"
  WHERE CC_CALL_cENTER_SK < 5 OR CC_CLASS = 'large';
```

### Logical Operators  IN, NOT IN
```
SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."CALL_CENTER"
    WHERE CC_CALL_cENTER_SK = '4' or CC_CALL_cENTER_SK = '12' or CC_CALL_cENTER_SK = '18'
        or CC_CALL_cENTER_SK = '24' or CC_CALL_cENTER_SK = '45';

SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."CALL_CENTER"
    WHERE CC_CALL_cENTER_SK IN (4,12,18,24,45) or CC_CLASS IN ('medium', 'large');

SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."CALL_CENTER"
    WHERE CC_CALL_cENTER_SK NOT IN (4,12,18,24,45);
```
### Logical Operator - Between
```
SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."CALL_CENTER"
    WHERE CC_CALL_CENTER_SK >= '4' and CC_CALL_CENTER_SK <= '9';

SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."CALL_CENTER"
    WHERE CC_CALL_CENTER_SK between '4' and '9';
```
### Logical Operator - Like
```
SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF1"."CUSTOMER"
    WHERE c_comment like 'a%';

```
### Logical Operator - Contains
```
SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF1"."CUSTOMER"
    WHERE contains (c_name, '134');
```

## GROUP BY  Aggregation function   (count  sum)   
```
select * from "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF001"."CUSTOMER";

select *,
    sum(c_acctbal) as acct_bal
from "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF001"."CUSTOMER"
group by c_mktsegment;
```

# ORDER BY
```
select * from "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF001"."ORDERS" order by o_orderpriority;

select * from "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF001"."ORDERS" order by o_orderpriority desc;
```

## HAVING
```
select c_mktsegment,
    sum(c_acctbal) as acct_bal
from "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF001"."CUSTOMER"
group by c_mktsegment
having acct_bal > 1280000;
```

#  Insert, Delete & Update Operations
```
    * INSERT – is used to insert data into a table.
    * UPDATE – is used to update existing data within a table.
    * DELETE – is used to delete records from a table.


create or replace table A(id number,
               name varchar(20));


select * from A;


insert into A values(1,'Aman'),
                    (2,'Bhavesh'),
                    (3,'Carolyn'),
                    (5,'David');
```
