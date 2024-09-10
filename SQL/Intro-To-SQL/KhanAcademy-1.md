# Basics

## Creating a table

ex:
```SQL
CREATE TABLE groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER);

INSERT INTO groceries VALUES (1, "Bananas",4 );
INSERT INTO groceries VALUES (2, "Oreo",4 );
INSERT INTO groceries VALUES (3, "Blue Berries",4 );

SELECT * FROM groceries;

CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT, rating NUMERIC);

INSERT INTO books VALUES (1, "a", 4.0);
INSERT INTO books VALUES (2, "b", 4.0);
INSERT INTO books VALUES (3, "c", 4.0);

SELECT * FROM books

```