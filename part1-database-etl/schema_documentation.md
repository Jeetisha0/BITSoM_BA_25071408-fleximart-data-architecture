# FlexiMart Database Schema Documentation

## Entity–Relationship Description (Text Format)

### ENTITY: customers
**Purpose:** Stores customer information for all registered users.

**Attributes:**
- customer_id: Unique identifier for each customer (Primary Key)
- first_name: Customer’s first name
- last_name: Customer’s last name
- email: Customer’s email address (unique)
- phone: Customer’s phone number
- city: City where the customer resides
- registration_date: Date when the customer registered on the platform

**Relationships:**
- One customer can place MANY orders (1:M relationship with orders table)

### ENTITY: products
**Purpose:** Stores details of products available for sale.

**Attributes:**
- product_id: Unique identifier for each product (Primary Key)
- product_name: Name of the product
- category: Category of the product (Electronics, Fashion, Groceries)
- price: Price of the product
- stock_quantity: Available quantity in stock

**Relationships:**
- One product can appear in MANY order items (1:M relationship with order_items table)



### ENTITY: orders
**Purpose:** Stores order-level information for customer purchases.

**Attributes:**
- order_id: Unique identifier for each order (Primary Key)
- customer_id: Identifier of the customer who placed the order (Foreign Key)
- order_date: Date when the order was placed
- total_amount: Total value of the order
- status: Order status (Completed, Pending, Cancelled)

**Relationships:**
- One order belongs to ONE customer (M:1 with customers table)
- One order can contain MANY order items (1:M with order_items table)


### ENTITY: order_items
**Purpose:** Stores item-level details of each order.

**Attributes:**
- order_item_id: Unique identifier for each order item (Primary Key)
- order_id: Identifier of the related order (Foreign Key)
- product_id: Identifier of the product ordered (Foreign Key)
- quantity: Number of units ordered
- unit_price: Price per unit at time of purchase
- subtotal: Total price for the item (quantity × unit_price)

**Relationships:**
- Each order item belongs to ONE order
- Each order item references ONE product


## Normalization Explanation (3NF)

The FlexiMart database design follows Third Normal Form (3NF) principles to ensure data integrity and reduce redundancy.  
Each table has a clearly defined primary key, and all non-key attributes are fully dependent on that primary key. For example, in the customers table, attributes such as first_name, last_name, email, and city depend only on customer_id and not on any other attribute.

There are no partial dependencies because all tables use single-column primary keys. Transitive dependencies are avoided by separating customer, product, and order information into different tables. Order-related details are stored in the orders table, while product-level details for each order are stored in the order_items table. This ensures that product information is not repeatedly stored for every order.

Functional dependencies include:
- customer_id → customer details
- product_id → product details
- order_id → order details
- order_item_id → quantity, unit_price, subtotal

This design avoids update anomalies by ensuring that changes to customer or product data need to be made in only one place. Insert anomalies are avoided because new customers or products can be added without requiring an order. Delete anomalies are prevented because deleting an order does not remove customer or product information.


## Sample Data Representation

### customers

| customer_id | first_name | last_name   | email                    | city       |
|------------ |----------- |-----------  |--------------------------|------------|
| 1           | Rahul      | Sharma      | rahul.sharma@gmail.com   | Bangalore  |
| 2           | Priya      | Patel       | priya.patel@yahoo.com    | Mumbai     |


### products

| product_id | product_name        | category     | price  | stock_quantity |
|----------- |---------------------|--------------|--------|----------------|
| 1          | Samsung Galaxy S21  | Electronics  | 45999  | 150            |
| 2          | Nike Running Shoes  | Fashion      | 3499   | 80             |


### orders

| order_id | customer_id | order_date | total_amount | status     |
|--------- |------------ |------------|--------------|------------|
| 1        | 1           | 2024-01-15 | 45999        | Completed  |
| 2        | 2           | 2024-01-16 | 5998         | Completed  |


### order_items

| order_item_id | order_id | product_id | quantity | unit_price | subtotal |
|-------------- |--------- |------------|----------|------------|----------|
| 1             | 1        | 1          | 1        | 45999      | 45999    |
| 2             | 2        | 2          | 2        | 2999       | 5998     |
