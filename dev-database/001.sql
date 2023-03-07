CREATE TABLE dbo.customers(
	id int NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	created_at DATETIME NOT NULL,
    PRIMARY KEY ( id )
);