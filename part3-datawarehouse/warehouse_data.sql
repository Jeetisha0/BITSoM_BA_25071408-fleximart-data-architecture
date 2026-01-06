
-- DIM_DATE (30 records)
-- January & February 2024

INSERT INTO dim_date VALUES
(20240101,'2024-01-01','Monday',1,1,'January','Q1',2024,0),
(20240102,'2024-01-02','Tuesday',2,1,'January','Q1',2024,0),
(20240103,'2024-01-03','Wednesday',3,1,'January','Q1',2024,0),
(20240104,'2024-01-04','Thursday',4,1,'January','Q1',2024,0),
(20240105,'2024-01-05','Friday',5,1,'January','Q1',2024,0),
(20240106,'2024-01-06','Saturday',6,1,'January','Q1',2024,1),
(20240107,'2024-01-07','Sunday',7,1,'January','Q1',2024,1),
(20240108,'2024-01-08','Monday',8,1,'January','Q1',2024,0),
(20240109,'2024-01-09','Tuesday',9,1,'January','Q1',2024,0),
(20240110,'2024-01-10','Wednesday',10,1,'January','Q1',2024,0),
(20240201,'2024-02-01','Thursday',1,2,'February','Q1',2024,0),
(20240202,'2024-02-02','Friday',2,2,'February','Q1',2024,0),
(20240203,'2024-02-03','Saturday',3,2,'February','Q1',2024,1),
(20240204,'2024-02-04','Sunday',4,2,'February','Q1',2024,1),
(20240205,'2024-02-05','Monday',5,2,'February','Q1',2024,0),
(20240206,'2024-02-06','Tuesday',6,2,'February','Q1',2024,0),
(20240207,'2024-02-07','Wednesday',7,2,'February','Q1',2024,0),
(20240208,'2024-02-08','Thursday',8,2,'February','Q1',2024,0),
(20240209,'2024-02-09','Friday',9,2,'February','Q1',2024,0),
(20240210,'2024-02-10','Saturday',10,2,'February','Q1',2024,1),
(20240211,'2024-02-11','Sunday',11,2,'February','Q1',2024,1),
(20240212,'2024-02-12','Monday',12,2,'February','Q1',2024,0),
(20240213,'2024-02-13','Tuesday',13,2,'February','Q1',2024,0),
(20240214,'2024-02-14','Wednesday',14,2,'February','Q1',2024,0),
(20240215,'2024-02-15','Thursday',15,2,'February','Q1',2024,0),
(20240216,'2024-02-16','Friday',16,2,'February','Q1',2024,0),
(20240217,'2024-02-17','Saturday',17,2,'February','Q1',2024,1),
(20240218,'2024-02-18','Sunday',18,2,'February','Q1',2024,1),
(20240219,'2024-02-19','Monday',19,2,'February','Q1',2024,0),
(20240220,'2024-02-20','Tuesday',20,2,'February','Q1',2024,0);



-- DIM_PRODUCT (15 records)

INSERT INTO dim_product (product_id, product_name, category, subcategory, unit_price) VALUES
('P001','Samsung Galaxy S21','Electronics','Smartphone',45999),
('P002','Nike Running Shoes','Fashion','Footwear',3499),
('P003','Apple MacBook Pro','Electronics','Laptop',52999),
('P004','Levis Jeans','Fashion','Clothing',2999),
('P005','Sony Headphones','Electronics','Audio',1999),
('P006','Organic Almonds','Groceries','Food',899),
('P007','HP Laptop','Electronics','Laptop',52999),
('P008','Adidas T-Shirt','Fashion','Clothing',1299),
('P009','Basmati Rice 5kg','Groceries','Food',650),
('P010','OnePlus Nord','Electronics','Smartphone',45999),
('P011','Puma Sneakers','Fashion','Footwear',4599),
('P012','Dell Monitor','Electronics','Monitor',12999),
('P013','Woodland Shoes','Fashion','Footwear',5499),
('P014','iPhone 13','Electronics','Smartphone',69999),
('P015','Organic Honey','Groceries','Food',450);


-- DIM_CUSTOMER (12 records)

INSERT INTO dim_customer (customer_id, customer_name, city, state, customer_segment) VALUES
('C001','Rahul Sharma','Bangalore','Karnataka','High Value'),
('C002','Priya Patel','Mumbai','Maharashtra','Medium Value'),
('C003','Amit Kumar','Delhi','Delhi','Medium Value'),
('C004','Sneha Reddy','Hyderabad','Telangana','High Value'),
('C005','Vikram Singh','Chennai','Tamil Nadu','Low Value'),
('C006','Anjali Mehta','Bangalore','Karnataka','Medium Value'),
('C007','Ravi Verma','Pune','Maharashtra','Low Value'),
('C008','Pooja Iyer','Bangalore','Karnataka','Medium Value'),
('C009','Karthik Nair','Kochi','Kerala','Low Value'),
('C010','Deepa Gupta','Delhi','Delhi','High Value'),
('C011','Arjun Rao','Hyderabad','Telangana','Medium Value'),
('C012','Lakshmi Krishnan','Chennai','Tamil Nadu','Low Value');


-- FACT_SALES (40 records)
INSERT INTO fact_sales
(date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount) VALUES
(20240101,1,1,1,45999,0,45999),
(20240102,2,2,2,3499,0,6998),
(20240103,3,3,1,52999,0,52999),
(20240104,4,4,2,2999,0,5998),
(20240105,5,5,3,1999,0,5997),
(20240106,6,6,5,899,0,4495),
(20240107,7,7,1,52999,0,52999),
(20240108,8,8,4,1299,0,5196),
(20240109,9,9,6,650,0,3900),
(20240110,10,10,1,45999,0,45999),

(20240201,11,11,2,4599,0,9198),
(20240202,12,12,1,12999,0,12999),
(20240203,13,1,1,5499,0,5499),
(20240204,14,2,1,69999,0,69999),
(20240205,15,3,3,450,0,1350),
(20240206,1,4,2,45999,0,91998),
(20240207,2,5,1,3499,0,3499),
(20240208,3,6,1,52999,0,52999),
(20240209,4,7,2,2999,0,5998),
(20240210,5,8,3,1999,0,5997),

(20240211,6,9,4,899,0,3596),
(20240212,7,10,1,52999,0,52999),
(20240213,8,11,2,1299,0,2598),
(20240214,9,12,5,650,0,3250),
(20240215,10,1,1,45999,0,45999),
(20240216,11,2,1,4599,0,4599),
(20240217,12,3,1,12999,0,12999),
(20240218,13,4,2,5499,0,10998),
(20240219,14,5,1,69999,0,69999),
(20240220,15,6,3,450,0,1350);
