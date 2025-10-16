BEGIN;
INSERT INTO orders (customer_id, total) VALUES (2, 5.00);
ROLLBACK;

BEGIN;
INSERT INTO orders (customer_id, total) VALUES (2, 5.00);
COMMIT;

SELECT COUNT(*) AS orders_for_grace FROM orders WHERE customer_id = 2;
