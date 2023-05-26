SELECT
customer.full_name AS NAME_CUSTOMER,
'order'.order_no AS ORDER_NUM
FROM 'order'
JOIN customer
ON 'order'.customer_id = customer.customer_id
WHERE 'order'.manager_id is NULL