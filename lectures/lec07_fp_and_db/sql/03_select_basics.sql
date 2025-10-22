SELECT * FROM orders;

SELECT id, total
FROM orders
WHERE total >= 9
ORDER BY total DESC
LIMIT 5;
