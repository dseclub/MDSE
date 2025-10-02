# DATE FUNCTIONS


## CURRENT_DATE, CURRENT_TIME, CURRENT_TIMESTAMP
```
select *,
    CURRENT_DATE() as today_date,
    CURRENT_TIME() as present_time,
    CURRENT_TIMESTAMP() as present_timestamp
    from "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF001"."CUSTOMER";
```
## DATE_PART: Extracts the specified date or time part from a date, time, or timestamp.
```
select *,
    CURRENT_TIMESTAMP() as present_timestamp,
    DATE_PART(hour, CURRENT_TIMESTAMP) as time_hours,
    DATE_PART(minute, CURRENT_TIMESTAMP) as time_minutes,
    DATE_PART(second, CURRENT_TIMESTAMP) as time_seconds,
    DATE_PART(year, CURRENT_TIMESTAMP) as year_,
    DATE_PART(quarter, CURRENT_TIMESTAMP) as quarter_,
    DATE_PART(month, CURRENT_TIMESTAMP) as month_
    from "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF001"."CUSTOMER";
```
## DATE_TRUNC: Truncates a DATE, TIME, or TIMESTAMP to the specified precision and is not the same as extraction

## TO_DATE, TO_TIMESTAMP, TO_TIME: Converts a string into respective format

## DAYNAME: Writes the current day of the week
```
SELECT TO_DATE('2020-06-22T23:39:18.245-09:00') AS "DATE1",
       DATE_TRUNC('YEAR', "DATE1") AS "TRUNCATED TO YEAR",
       DATE_TRUNC('MONTH', "DATE1") AS "TRUNCATED TO MONTH",
       DATE_TRUNC('DAY', "DATE1") AS "TRUNCATED TO DAY",
       DAYNAME(DATE1) as CURRENT_DAY;

SELECT TO_TIMESTAMP('2020-06-22T23:39:18.245-09:00') AS "TIMESTAMP1",
        DATE_TRUNC('HOUR', "TIMESTAMP1") AS "TRUNCATED TO HOUR",
       DATE_TRUNC('MINUTE', "TIMESTAMP1") AS "TRUNCATED TO MINUTE",
       DATE_TRUNC('SECOND', "TIMESTAMP1") AS "TRUNCATED TO SECOND";

SELECT TO_TIME('23:39:20.123') AS "TIME1",
       DATE_TRUNC('MINUTE', "TIME1") AS "TRUNCATED TO MINUTE";
```

## DATEADD: Adds the specified value for the specified date or time part to a date, time, or timestamp.
```
create table test_dates as
select *,
        dateadd(year, 5, o_orderdate) as new_orderdate_year,
        dateadd(month, 7, o_orderdate) as new_orderdate_month,
        dateadd(quarter, 1, o_orderdate) as new_orderdate_quarter
from "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF001"."ORDERS";

select * from test_Dates;
```
## DATEDIFF: Calculates the difference between two date, time, or timestamp expressions based on the date or time part requested.
          -- The function returns the result of subtracting the second argument from the third argument.
          -- The minus sign (“-“) can also be used to subtract dates.
```
select * from test_dates;

select o_orderdate, new_orderdate_year, datediff(year, o_orderdate, new_orderdate_year) as diff_year,
        o_orderdate, new_orderdate_month, datediff(month, o_orderdate, new_orderdate_month) as diff_month,
        o_orderdate, new_orderdate_quarter, datediff(quarter, o_orderdate, new_orderdate_quarter) as diff_quarter
from test_dates limit 10;
```
