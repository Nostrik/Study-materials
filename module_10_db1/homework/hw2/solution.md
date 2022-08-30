## Исследование продаж телефонов

### 1.Телефоны какого цвета чаще всего покупают?

Необходимо создать запрос, который из таблицы table_checkout
по маскимальному значению столбца phone_id найдет модель телефона
в поле name из таблицы table_phones.

SELECT name
FROM table_phones
WHERE id == (SELECT max(phone_id) FROM table_checkout)

Ответ: Samsung Neo i

### 2.Какие телефоны чаще покупают: красные или синие?

