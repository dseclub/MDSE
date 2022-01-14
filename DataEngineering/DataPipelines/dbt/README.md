# DBT 

Data build tool is a framework that allows data teams to quickly iterate on building data transformation pipelines using templated SQL.

dbt allows you to develop, document, test, deploy data in the data warehouse.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

## dbt (Data Build Tool)
### 1 Quickly and easily provide clean, transformed data ready for analysis:
dbt enables data analysts to custom-write transformations through SQL SELECT statements. There is no need to write boilerplate code. This makes data transformation accessible for analysts that don’t have extensive experience in other programming languages.

### 2 Apply software engineering practices—such as modular code, version control, testing, and continuous integration/continuous deployment (CI/CD)—to analytics code: 
Continuous integration means less time testing and quicker time to development, especially with dbt Cloud. You don’t need to push an entire repository when there are necessary changes to deploy, but rather just the components that change. You can test all the changes that have been made before deploying your code into production. dbt Cloud also has integration with GitHub for automation of your continuous integration pipelines, so you won’t need to manage your own orchestration, which simplifies the process.

### 3 Build reusable and modular code using Jinja. 
dbt (data build tool) allows you to establish macros and integrate other functions outside of SQL’s capabilities for advanced use cases. Macros in Jinja are pieces of code that can be used multiple times. Instead of starting at the raw data with every analysis, analysts instead build up reusable data models that can be referenced in subsequent work.

### 4 Maintain data documentation and definitions within dbt as they build and develop lineage graphs:
Data documentation is accessible, easily updated, and allows you to deliver trusted data across the organization. dbt (data build tool) automatically generates documentation around descriptions, models dependencies, model SQL, sources, and tests. dbt creates lineage graphs of the data pipeline, providing transparency and visibility into what the data is describing, how it was produced, as well as how it maps to business logic.

### 5 Perform simplified data refreshes within dbt Cloud:
There is no need to host an orchestration tool when using dbt Cloud. It includes a feature that provides full autonomy with scheduling production refreshes at whatever cadence the business wants.

### 6 Perform automated testing:
dbt (data build tool) comes prebuilt with unique, not null, referential integrity, and accepted value testing. Additionally, you can write your own custom tests using a combination of Jinja and SQL. To apply any test on a given column, you simply reference it under the same YAML file used for documentation for a given table or schema. This makes testing data integrity an almost effortless process.

https://github.com/dbt-labs/dbt

https://docs.getdbt.com/reference/resource-configs/redshift-configs

https://docs.getdbt.com/reference/resource-configs/snowflake-configs

https://docs.getdbt.com/reference/dbt-jinja-functions

https://docs.getdbt.com/docs/running-a-dbt-project/running-dbt-in-production


## Training

https://courses.getdbt.com/courses/fundamentals

