# NoSQL Analysis for FlexiMart

## Section A: Limitations of RDBMS 

- Relational databases such as MySQL are well suited for structured and stable data, but they face limitations when handling highly diverse product information. In an e-commerce platform like FlexiMart, different products require different attributes. For example, laptops have specifications like RAM and processor, while shoes require size and color. Representing this diversity in a relational database requires multiple tables or many nullable columns, which increases schema complexity.

- Frequent schema changes are another challenge. Introducing new product types often requires altering table structures, which can be risky and time-consuming. Additionally, storing customer reviews in a relational database typically involves separate tables and joins. This increases query complexity and can reduce performance when fetching product details along with reviews.

- Overall, relational databases struggle with flexibility and scalability when dealing with evolving and semi-structured product data.


## Section B: Benefits of NoSQL (MongoDB) 

- MongoDB addresses these challenges by using a flexible, document-oriented data model. Each product is stored as a document, allowing different products to have different attributes without enforcing a fixed schema. This makes it easy to add new product types or attributes without modifying existing data structures.

- MongoDB supports embedded documents, which allows customer reviews to be stored directly within product documents. This simplifies data retrieval and improves read performance, especially for applications that frequently display product details along with reviews.

- Another key benefit of MongoDB is horizontal scalability. It can distribute data across multiple servers, making it suitable for large and growing product catalogs. These features make MongoDB a strong choice for managing flexible and fast-changing product data in an e-commerce environment.


## Section C: Trade-offs of MongoDB 

- Disadvantage of MongoDB is the lack of built-in relational constraints such as foreign keys, which means data consistency must be managed at the application level. This can increase development responsibility and the risk of inconsistent data.

- Another limitation is that complex analytical queries involving multiple collections are generally easier to perform in relational databases using SQL. As a result, MongoDB is best used alongside relational databases rather than completely replacing them for transactional and analytical workloads.
