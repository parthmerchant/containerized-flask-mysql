--This creates and uses our database
CREATE DATABASE local-mysql;
USE local-mysql;

--This creates our items table
CREATE TABLE 'items' (
	'id' int unsigned NOT NULL AUTO_INCREMENT,
	'name' varchar(50) NOT NULL,
	'price' float NOT NULL,
	'quantity' int NOT NULL,
	PRIMARY KEY ('id')
);

INSERT INTO 'items' ('id', 'product_name', 'price', 'quantity') VALUES
('Computer Monitor', 200.00, 20),
('Desk', 50.00, 10),
('Smartphone', 1000.00, 5);
