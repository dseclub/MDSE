# Materialized Views

![Materialized Views](../pics/MaterializedViews.PNG)

**Materialized views:**

A materialized view contains a precomputed result set, based on an SQL query over one or more base tables.

Materialized views are especially useful for speeding up queries that are predictable and repeated.

With support for materialized views, Amazon Redshift provides significantly faster query performance for predictable and repeated workloads such as ELT data processing and BI dashboards.

You can use materialized views to easily store and manage pre-computed results of a SELECT statement that may reference one or more tables, including external tables. Subsequent queries referencing the materialized views can run much faster by reusing the pre-computed results. Amazon Redshift can efficiently maintain the materialized views incrementally to continue to provide the low latency performance benefits.

https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html

https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-create-sql-command.html

Automated Materialized View (AutoMV) for Amazon Redshift helps lower query latency for repeatable workloads like dashboard queries minimizing the effort for manually creating and managing materialized views. 

Materialized Views are a powerful tool for improving query performance but they require careful workload monitoring and analysis to determine where they may provide the best returns. This may take hours to days and require performance tuning knowledge. Additionally, increasing and changing workloads results in continual monitoring by users.

AutoMV in Amazon Redshift continually monitors the workload using machine learning to decide whether a new materialized view will be beneficial.

AutoMV balances the cost of creating and keeping materialized views up-to-date vs expected improvements to query latency. The system also monitors previously created AutoMVs and drops them when they are no longer beneficial to the workload. This avoids expending resources to keep unused AutoMVs fresh.
