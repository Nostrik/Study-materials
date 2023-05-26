SELECT DISTINCT city
FROM customer;

--множество уникальных значений
SELECT DISTINCT city,
                full_name
FROM customer;

--количество записей
SELECT count(*)
FROM orders;

--кол-во, где стоимость больше 800 и меньше 900
SELECT count(*)
FROM orders
WHERE purchase_amount > 800
  AND purchase_amount < 900;

--среднее значение
SELECT avg(purchase_amount)
FROM orders;

--округление значения до целой части
SELECT round(avg(purchase_amount)) AS average_purchase_amount
FROM orders;

--комулятивная сумма значений
SELECT sum(purchase_amount) AS total_amount
FROM orders;

--максимальная сумма продажи
SELECT max(purchase_amount) AS max_purchase
FROM orders;

--менеждер, соверщивший макс количество продаж
SELECT max(purchase_amount) AS max_purchase,
       m.full_name
FROM orders o
INNER JOIN manager m ON m.manager_id = o.manager_id;

--минимальная продажа и виновник минимальной продажи
SELECT min(purchase_amount) AS max_purchase,
       m.full_name
FROM orders o
INNER JOIN manager m ON m.manager_id = o.manager_id;

--список всех сотрудников, разделенных запятой
SELECT sum(full_name)
FROM manager;