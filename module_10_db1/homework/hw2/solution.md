## Исследование продаж телефонов

### 1.Телефоны какого цвета чаще всего покупают?

Необходимо создать запрос, который из таблицы table_checkout
по маскимальному значению столбца phone_id найдет модель телефона
в поле name из таблицы table_phones.

SELECT name
FROM table_phones
WHERE id = (SELECT max(phone_id) FROM table_checkout)

Ответ: Samsung Neo i

### 2.Какие телефоны чаще покупают: красные или синие?

Необходимо выбрать из таблицы table_phones id телефонов нужных цветов.
Затем, посчитать количество проданных экземпляров одного цвета и другого и сравнить.

SELECT id
FROM table_phones
WHERE colour == "красный"

id(красный цвет):3, 7, 9

SELECT id
FROM table_phones
WHERE colour == "синий"

id(синий цвет):1, 6, 8

Далее подставим каждый id каждого цвета в запрос:

SELECT count(*)
FROM table_checkout
WHERE phone_id = color

Для красного:

SELECT count(*)
FROM table_checkout
WHERE phone_id = 3, count = 141 

SELECT count(*)
FROM table_checkout
WHERE phone_id = 7, count = 163

SELECT count(*)
FROM table_checkout
WHERE phone_id = 9, count = 125

Для синего:

SELECT count(*)
FROM table_checkout
WHERE phone_id = 1, count = 176

SELECT count(*)
FROM table_checkout
WHERE phone_id = 6, count = 160

SELECT count(*)
FROM table_checkout
WHERE phone_id = 8, count = 164

Ответ: 141 + 163 + 125 = 429, 176 + 160 + 164 = 500;
Телефонов синего цвета продано больше.

### 3.Какой самый непопулярный цвет телефона?

Необходимо узнать количество проданных телефонов, оставшихся цветов.

SELECT id
FROM table_phones
WHERE colour == "золотой"

id(золотой цвет):2

SELECT id
FROM table_phones
WHERE colour == "голубой"

id(голубой цвет):4, 5

Для золотого:

SELECT count(*)
FROM table_checkout
WHERE phone_id = 2, count = 28

Для голубого:

SELECT count(*)
FROM table_checkout
WHERE phone_id = 4, count = 20

SELECT count(*)
FROM table_checkout
WHERE phone_id = 5, count = 23

Ответ: самый непопулярный цвет, золотой.
