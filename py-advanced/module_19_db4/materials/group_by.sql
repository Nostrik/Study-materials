--сгруппировать покупки по менеджерам и посчитать сумму покупок каждого
SELECT sum(purchase_amount),
       manager_id
FROM orders
GROUP BY manager_id;

--сгруппировать покупки по менеджерам и посчитать сумму покупок каждого, + имена менеджеров
SELECT sum(purchase_amount),
       full_name
FROM orders
LEFT OUTER JOIN manager m ON m.manager_id = orders.manager_id
GROUP BY orders.manager_id;


SELECT sum(purchase_amount),
       full_name
FROM orders
LEFT OUTER JOIN manager m ON m.manager_id = orders.manager_id
GROUP BY orders.manager_id;

--среднне значение продаж каждого менеджера
SELECT avg(purchase_amount),
       full_name
FROM orders
LEFT OUTER JOIN manager m ON m.manager_id = orders.manager_id
GROUP BY orders.manager_id;

--сколько тратят покупатели в разных городах
SELECT purchase_amount,
       manager_id
FROM orders
GROUP BY manager_id,
         purchase_amount
SELECT city,
       avg(purchase_amount) avg_purchase
FROM customer
INNER JOIN orders o ON customer.customer_id = o.customer_id
GROUP BY city
ORDER BY avg_purchase DESC;

--все продавцы, кто совершил больше 500 продаж
SELECT full_name,
       count(purchase_amount) AS cnt_purchases
FROM orders
INNER JOIN manager m ON m.manager_id = orders.manager_id
GROUP BY full_name
HAVING cnt_purchases > 500;


SELECT full_name,
       count(purchase_amount) AS cnt_purchases
FROM orders
INNER JOIN manager m ON m.manager_id = orders.manager_id
GROUP BY full_name
HAVING full_name like 'Пет%';


SELECT full_name,
       count(purchase_amount) AS cnt_purchases
FROM orders
INNER JOIN manager m ON m.manager_id = orders.manager_id
WHERE full_name like 'Пет%'
GROUP BY full_name
