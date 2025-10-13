-- 'name' is UNIQUE, so this will insert or do nothing if it exists
INSERT INTO customer (name) VALUES ('Ada')
ON CONFLICT(name) DO NOTHING;

-- Or update the name if you prefer:
INSERT INTO customer (name) VALUES ('Grace')
ON CONFLICT(name) DO UPDATE SET name = excluded.name;
