SELECT * FROM public.groceries
ORDER BY id;


INSERT INTO groceries (product, type, price) VALUES
('banana', 'fruit', 5),
('apple', 'fruit', 3),
('korn', 'vegetables', 9),
('tomato', 'vegetables', 12),
('coca cola', 'drinks', 20);

UPDATE groceries SET country_of_origin = 'Ukraine' WHERE type = 'vegetables';
DELETE FROM groceries WHERE type = 'drinks';

CREATE TABLE IF NOT EXISTS groceries (
    product varchar NOT NULL,
    type varchar(30) NOT NULL,
    price int NOT NULL,
    country_of_origin varchar,
    id serial NOT NULL UNIQUE,
    PRIMARY KEY (id)
);







