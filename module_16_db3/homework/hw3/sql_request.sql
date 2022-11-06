SELECT
customer.full_name as CUSTOMER,
manager.full_name as MANAGER,
purchase_amount as PURCHASE_AMOUNT,
date as DATE
FROM 'order' JOIN manager on 'order'.manager_id = manager.manager_id
JOIN customer on 'order'.customer_id = customer.customer_id