-- =====================================================
-- FlexiMart – Part 1.3 Business Query Implementation
-- =====================================================

USE fleximart;

-- -----------------------------------------------------
-- Query 1: Customer Purchase History
-- -----------------------------------------------------

SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.email,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.subtotal) AS total_spent
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY
    c.customer_id, c.first_name, c.last_name, c.email
HAVING
    COUNT(DISTINCT o.order_id) >= 2
    AND SUM(oi.subtotal) > 5000
ORDER BY
    total_spent DESC;
