CREATE TABLE customers (
    ID int AUTO_INCREMENT PRIMARY KEY,
    NAMAID varchar(255) NOT NULL,
    NAMALENGKAP varchar(255) NOT NULL,
    EMAIL varchar(255) NOT NULL,
    UNIQUE (NAMAID, EMAIL)
);


INSERT INTO customers (NAMAID, NAMALENGKAP, EMAIL) 
values ("Astrid", "Astrid Gruber", "astrid.gruber@apple.at")
;

