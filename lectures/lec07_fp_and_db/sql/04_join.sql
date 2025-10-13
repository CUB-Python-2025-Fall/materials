SELECT o.id AS order_id,
       c.name AS customer,
       o.created_at,
       o.total
FROM orders o
JOIN customer c ON c.id = o.customer_id
ORDER BY o.created_at;
