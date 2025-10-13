-- drop tables if they exist (just to reset the database)
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customer;


CREATE TABLE IF NOT EXISTS customer (  -- note: there's no need for IF NOT EXISTS here
  id   INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS orders (
  id          INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  created_at  TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  total       REAL    NOT NULL CHECK(total >= 0),
  FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);
