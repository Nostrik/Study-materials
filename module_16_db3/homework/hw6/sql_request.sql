SELECT
customer.full_name as CUSTOMER,
'order'.purchase_amount as AMOUNT
FROM customer
JOIN 'order' on 'order'.customer_id = customer.customer_id
ORDER BY AMOUNT DESC