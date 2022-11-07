SELECT
order_no as ORDER_NUM,
customer.full_name as CUSTOMER,
manager.full_name as MANAGER
FROM 'order'
JOIN manager
on 'order'.manager_id = manager.manager_id
JOIN customer
on 'order'.customer_id = customer.customer_id
WHERE customer.city != manager.city
