-- Query 1: Monthly Sales Drill-Down Analysis
-- Business Scenario:
-- The CEO wants to analyze sales starting from year,
-- drilling down to quarter and then month for 2024.
-- Demonstrates: Year → Quarter → Month drill-down

SELECT
    d.year,
    d.quarter,
    d.month_name,
    SUM(f.total_amount) AS total_sales,
    SUM(f.quantity_sold) AS total_quantity
FROM fact_sales f
JOIN dim_date d
    ON f.date_key = d.date_key
WHERE d.year = 2024
GROUP BY d.year, d.quarter, d.month, d.month_name
ORDER BY d.year, d.quarter, d.month;


-- Query 2: Top 10 Products by Revenue
-- Business Scenario:
-- Identify the top-performing products based on revenue.
-- Includes revenue contribution percentage.

SELECT
    p.product_name,
    p.category,
    SUM(f.quantity_sold) AS units_sold,
    SUM(f.total_amount) AS revenue,
    ROUND(
        (SUM(f.total_amount) / 
        (SELECT SUM(total_amount) FROM fact_sales)) * 100,
        2
    ) AS revenue_percentage
FROM fact_sales f
JOIN dim_product p
    ON f.product_key = p.product_key
GROUP BY p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;

-- Query 3: Customer Segmentation Analysis
-- Business Scenario:
-- Segment customers into High, Medium, and Low value
-- based on their total spending.
-- =========================================

WITH customer_spending AS (
    SELECT
        c.customer_key,
        SUM(f.total_amount) AS total_spent
    FROM fact_sales f
    JOIN dim_customer c
        ON f.customer_key = c.customer_key
    GROUP BY c.customer_key
)

SELECT
    CASE
        WHEN total_spent > 50000 THEN 'High Value'
        WHEN total_spent BETWEEN 20000 AND 50000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS customer_segment,
    COUNT(*) AS customer_count,
    SUM(total_spent) AS total_revenue,
    ROUND(AVG(total_spent), 2) AS avg_revenue
FROM customer_spending
GROUP BY customer_segment;
