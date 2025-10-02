# Stored Procedures

### Overview of stored procedures in Amazon Redshift

Stored procedures are commonly used to encapsulate logic for data transformation, data validation, and business-specific logic.

By combining multiple SQL steps into a stored procedure, you can reduce round trips between your applications and the database.

For fine-grained access control, you can create stored procedures to perform functions without giving a user access to the underlying tables. For example, only the owner or a superuser can truncate a table, and a user needs write permission to insert data into a table. Instead of granting a user permissions on the underlying tables, you can create a stored procedure that performs the task. You then give the user permission to run the stored procedure.

A stored procedure with the DEFINER security attribute runs with the privileges of the stored procedure's owner. By default, a stored procedure has INVOKER security, which means the procedure uses the permissions of the user that calls the procedure.

To create a stored procedure, use the CREATE PROCEDURE command. To run a procedure, use the CALL command.


You can define an Amazon Redshift stored procedure using the PostgreSQL procedural language PL/pgSQL to perform a set of SQL queries and logical operations. The procedure is stored in the database and is available for any user with sufficient privileges to run.

Unlike a user-defined function (UDF), a stored procedure can incorporate data definition language (DDL) and data manipulation language (DML) in addition to SELECT queries. A stored procedure doesn't need to return a value. You can use procedural language, including looping and conditional expressions, to control logical flow.



```
CREATE OR REPLACE PROCEDURE test()
AS $$
BEGIN
  SELECT 1 a;
END;
$$
LANGUAGE plpgsql
;
/
```

```
CREATE OR REPLACE PROCEDURE test_sp2(f1 IN int, f2 INOUT varchar(256), out_var OUT varchar(256))
AS $$
DECLARE
  loop_var int;
BEGIN
  IF f1 is null OR f2 is null THEN
    RAISE EXCEPTION 'input cannot be null';
  END IF;
  DROP TABLE if exists my_etl;
  CREATE TEMP TABLE my_etl(a int, b varchar);
    FOR loop_var IN 1..f1 LOOP
        insert into my_etl values (loop_var, f2);
        f2 := f2 || '+' || f2;
    END LOOP;
  SELECT INTO out_var count(*) from my_etl;
END;
$$ LANGUAGE plpgsql;


call test_sp2(2,'2019');

         f2          | column2
---------------------+---------
 2019+2019+2019+2019 | 2
(1 row)
```

## Ref

https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-overview.html
