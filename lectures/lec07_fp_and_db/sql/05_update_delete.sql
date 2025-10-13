-- Give order #1 a new total
UPDATE orders SET total = 12.00 WHERE id = 1;

-- Delete customer 'Ada' and watch her orders disappear (cascade)
DELETE FROM customer WHERE name = 'Ada';

-- Check what's left
SELECT * FROM customer;
SELECT * FROM orders;
