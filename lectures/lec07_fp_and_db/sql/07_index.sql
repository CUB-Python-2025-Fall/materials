CREATE INDEX IF NOT EXISTS idx_orders_customer_created
ON orders(customer_id, created_at);

EXPLAIN QUERY PLAN
SELECT *
FROM orders
WHERE customer_id = 2
ORDER BY created_at DESC;
