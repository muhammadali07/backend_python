-- Simple Select
SELECT customerNumber, customerName 
FROM customers
;

SELECT * 
FROM customers
;

-- select - where 
SELECT customerNumber as id, customerName as name
FROM customers
WHERE 
	125 < customerNumber and customerNumber < 150
;

-- select - join
select * 
from orders
Limit 10
;


select * 
from orders a
inner join customers b on a.customerNumber = b.customerNumber
Limit 10
;


