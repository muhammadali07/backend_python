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

-- insert banyak
INSERT INTO customers (NAMAID, NAMALENGKAP, EMAIL) 
values 
("Fernanda","Fernanda Ramos","fernadaramos4@uol.com.br"),
("Mark","Mark Philips","mphilips12@shaw.ca"),
("Jennifer","Jennifer Peterson","jenniferp@rogers.ca")
;

-- mengubah data 
UPDATE customers 
SET 
    NAMALENGKAP = "Jennifer Lauren",
    EMAIL = "jenniferl@rogers.ca"
WHERE
    ID = 4
;

-- menghapus data 
DELETE FROM customers
WHERE ID = 4
;