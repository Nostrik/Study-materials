
SELECT count(order_no)
FROM   orders
WHERE  manager_id = (SELECT manager_id
                     FROM   manager
                     WHERE  full_name LIKE 'Семёнов%');



SELECT count(order_no)
FROM orders
JOIN manager m ON m.manager_id = orders.manager_id
WHERE m.full_name like 'Семёнов%';

--имена всех продавцов, кто не живет в мосвке
SELECT full_name
FROM manager
WHERE city in
    (SELECT DISTINCT city
     FROM manager
     WHERE city != 'Москва' );

--имена покупателенй, которые совершили покупку больше чем на 900
SELECT full_name
FROM customer
WHERE customer_id in
    (SELECT customer_id
     FROM orders
     WHERE purchase_amount > 900 )


--номер заказа, имя мэнеджера и имя покупателя, которые проживают в одном городе
SELECT order_no,
       manager_name,
       customer_name
FROM orders
INNER JOIN
  (SELECT m.full_name AS manager_name,
          manager_id AS man_id,
          city AS c_city
   FROM manager m) ON orders.manager_id = man_id
INNER JOIN
  (SELECT full_name AS customer_name,
          customer_id AS cus_id,
          city AS m_city
   FROM customer c) ON cus_id = orders.customer_id
WHERE c_city == m_city;

--10 самых проследних продаж с именами менеджеров, где сумма продажи была более 900
SELECT full_name, date, amount
FROM manager
INNER JOIN
  (SELECT date AS date,
          purchase_amount AS amount,
          manager_id AS man_id
   FROM orders) ON manager_id = man_id
WHERE amount > 900
ORDER BY date DESC
LIMIT 10;

--все покупатели, у которых инициалы совпадат с инициалами одно из менеджеров
SELECT full_name
FROM customer
WHERE exists
    (SELECT full_name AS m_name
     FROM manager
     WHERE full_name like '%' || substr(full_name, -4) );