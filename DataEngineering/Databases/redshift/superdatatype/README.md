# Amazon Redshift Super datatype

Amazon Redshift Super datatype, a generic datatype within redshift that enables use of document/object formats, reducing pre/post processing needs.


The SUPER data type is an Amazon Redshift data type that enables the storage of schemaless arrays and structures that contain Amazon Redshift scalars and possibly nested arrays and structures. Use the SUPER data type to store semistructured data or documents as values.

With the SUPER data type and the PartiQL language, Amazon Redshift expands data warehouse capabilities to natively ingest, store, transform, and analyze semi-structured data.

https://docs.aws.amazon.com/redshift/latest/dg/super-overview.html

https://aws.amazon.com/blogs/big-data/work-with-semistructured-data-using-amazon-redshift-super/

https://docs.aws.amazon.com/redshift/latest/dg/super-configurations.html

AWS What's Next ft. SUPER Data Type for Amazon Redshift  Jun 15, 2021
https://www.youtube.com/watch?v=Dqrdhpc95vI

![Super datatype](superdatatype.PNG)

https://docs.aws.amazon.com/redshift/latest/dg/limitations-super.html

- You can't define SUPER columns as either a distribution or sort key.

- The SUPER data type only supports up to 1MB of data for an individual SUPER object.

- An individual value within a SUPER object is limited to the maximum length of the corresponding Amazon Redshift type. For example, a single string value loaded to SUPER is limited to the maximum VARCHAR length of 65535 bytes.

- You can't perform partial update or transform operations on SUPER columns.

- You can't use the SUPER data type and its alias in right joins or full outer joins.

- The SUPER data type doesn't support XML as inbound or outbound serialization format.

- In the FROM clause of a subquery (that is correlated or not) that references a table variable for unnesting, the query can only refer to its parent table and not other tables.

- Casting limitations
