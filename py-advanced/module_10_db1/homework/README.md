## Практическая работа 10
### Цель практической работы
* Познакомиться с реляционными базами данных.
* Научиться:
  * работать с БД из IDE,
  * работать с БД из Python с помощью модуля sqlite3.
* Попрактиковаться в написании SQL-запросов.

### Что входит в практическую работу
1. Посетители автосалона.
2. Исследование продаж телефонов.
3. Анализ таблиц.
4. Исследование доходов населения.
5. Быстрая вставка.

## Задача 1. Посетители автосалона
### Что нужно сделать

В репозитории находится БД посетителей автосалона — `hw_1_database.db.`

Внесите туда данные о следующих машинах:

| №   | Номер авто | Название авто     | Описание                                              | Владелец         |
|-----|------------|-------------------|-------------------------------------------------------|------------------|
| 1   | У314ОМ77   | Chevrolet         | Помятый задний бампер                                 | Киприянов А. И.  |
| 2   | О006ОО178  | Lorraine-Dietrich | Царапины на левом крыле                               | Петриенко М. Ю.  |
| 3   | К994ХЕ78   | Tesla             | Только с завода                                       | Петриенко М. Ю.  |
| 4   | С569ТВ78   | Lorraine-Dietrich | Помятая левая дверь, царапина на переднем бампере     | Комаренко И. П.  |
| 5   | С614СА23   | Alfa Romeo        | Лобовое стекло в трещинах                             | Шарко П. К.      |
| 6   | С746ОР78   | Tesla             | Только с завода, проблема с документами               | Петриенко М. Ю.  |
| 7   | Н130КЕ777  | Lorraine-Dietrich | Раритетная модель, перебрать двигатель                | Силагадзе Л. С.  |
| 8   | Н857СК27   | Lada              | Не заводится, без внешних повреждений                 | Петриенко М. Ю.  |
| 9   | У657СА77   | Lada              | Не читается VIN                                       | Киприянов А. И.  |
| 10  | Е778ВЕ178  | Ford              | Поменять габаритные лампы, резину на зимнюю           | Яковлева Е. А.   |
| 11  | К886УН68   | Lada              | Клиент жаловался на тёмные выхлопы при езде в городе  | Смитенко С. С.   |
| 12  | Н045МО97   | Lada              | Разбита левая фара, помят передний бампер             | Силагадзе Л. С.  |
| 13  | Т682КО777  | Alfa Romeo        | Поменять резину на зимнюю. Царапина на капоте (?)     | Яковлева Е. А.   |
| 14  | О147НМ78   | Chevrolet         | Провести ТО №9                                        | Шарко П. К.      |
| 15  | К110ТА77   | Lada              | Развал-схождение + замена резины                      | Смитенко С. С.   |
| 16  | Е717ОЕ78   | Chevrolet         | Помята водительская дверь, заменить габаритки         | Шарко П. К.      |
| 17  | У261ХО57   | Ford              | Заменить резину, проверить свечи                      | Петриенко М. Ю.  |
| 18  | М649ОМ78   | Alfa Romeo        | Непонятные шумы при заводе                            | Киприянов А. И.  |
| 19  | С253НО90   | Ford              | Заменить аккумулятор, проверить свечи                 | Комаренко И. П.  |
| 20  | А757АХ11   | Nissan            | ТО, клиент жалуется, что машину косит влево           | Глухих К. И.     |

В качестве решения приложите скриншот с данными таблицы `table_car`.

### Советы и рекомендации
IDE поддерживает вставку сразу нескольких строк. Для этого нужно нажать _Add row_ и 
вставить скопированную таблицу.
### Что оценивается
* Поле `belongs_to` указывает на ID владельца.
* Таблица `table_car` содержит все записи, данные в условии.
* Внесённые изменения применены с помощью *Submit*.

## Задача 2. Исследование продаж телефонов
### Что нужно сделать

Представьте, что вы работаете программистом в крупной сети розничных продаж телефонов. К вам пришли из отдела маркетинга и поставили задачу выяснить соотношение продаж телефонов
в зависимости от их цвета. 

Откройте в IDE БД `hw_2_database.db`. Используя таблицы `table_checkout` и `table_phones`, найдите ответы на следующие вопросы:

1. Телефоны какого цвета чаще всего покупают?
2. Какие телефоны чаще покупают: красные или синие?
3. Какой самый непопулярный цвет телефона?

Представьте ответы на вопросы в виде файла `report.md` с кратким описанием решения.
### Советы и рекомендации
SQL-запросы к БД можно отправлять прямо в IDE. [Инструкция](https://www.jetbrains.com/help/pycharm/working-with-database-consoles.html).
### Что оценивается
* Решение оформлено в виде Markdown-файла.
* Имеются обоснования, содержащие конкретные цифры.

## Задача 3. Анализ таблиц
### Что нужно сделать

Попрактикуемся в работе с БД из Python.

Есть база данных `hw_3_database.db`, в которой находятся три таблицы:
`table_1`, `table_2` и `table_3`. Каждая таблица имеет структуру из двух столбцов: `id` (число) и `value` (строка).

Выполните запросы, которые дадут ответы на следующие вопросы:

1. Сколько записей (строк) хранится в каждой таблице?
2. Сколько в таблице `table_1` уникальных записей?<br>Назовём уникальной такую запись, которая ранее не встречалась в таблице.
3. Как много записей из таблицы `table_1` встречается в `table_2`?
4. Как много записей из таблицы `table_1` встречается и в `table_2`, и в `table_3`?

### Советы и рекомендации
* Получить записи из таблицы можно так:
  ```python
  import sqlite3
  
  with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `some_database_table_name`")
    result = cursor.fetchall()
  ``` 
* Для получения уникальных записей можно воспользоваться [DISTINCT](https://www.sqlitetutorial.net/sqlite-distinct/).
* Если нужно ответить на вопрос «сколько?», необязательно получать из таблицы все строки. Достаточно добавить в SQL запрос [COUNT](https://www.sqlitetutorial.net/sqlite-count-function/).
* Для нахождения пересечения таблиц поможет [INTERSECT](https://www.sqlitetutorial.net/sqlite-intersect/) или [JOIN](https://www.sqlitetutorial.net/sqlite-join/).

### Что оценивается
* Python не производит никаких операций над полученными строками. В большей мере используются возможности SQL-запросов.
* Все запросы делаются в рамках одного подключения к БД.


## Задача 4. Исследование доходов населения
### Что нужно сделать
Представьте, что вы работаете в отделе статистики и учёта островного государства N. Вам поступило задание на крупное исследование касаемо доходов населения.

С помощью работы БД из Python вам нужно выполнить следующие задания:

1. Выяснить, сколько человек с острова N находятся за чертой бедности, то есть получает меньше 5000 гульденов в год.
2. Посчитать среднюю зарплату по острову N.
3. Посчитать медианную зарплату по острову. 
4. Посчитать число социального неравенства F, определяемое как `F = T/K`, где `T` — суммарный доход 10% самых обеспеченных жителей острова `N, K` — суммарный доход остальных 90% людей. Вывести ответ в процентах с точностью до двух знаков после запятой.

Обезличенную БД жителей острова N вы можете найти в файле `hw_4_database.db`. В таблице `salaries` находятся уникальные идентификаторы людей и их заработные платы.

_Опционально_. Для решения задачи 4 используйте только один SQL-запрос.

### Советы и рекомендации
* Медианная зарплата — это величина, которая делит население на две равные части: 50% получают зарплату ниже этого значения и 50% — выше.
* Для решения пригодятся функции [AVG](https://www.sqlitetutorial.net/sqlite-avg/), [SUM](https://www.sqlitetutorial.net/sqlite-sum/), [ROUND](https://www.sqlitetutorial.net/sqlite-functions/sqlite-round/) и [CAST](https://www.w3schools.com/sql/func_sqlserver_cast.asp).
* Чтобы составить сложный SQL-запрос, разложите его на более простые. Например, для решения опционального задания разложение может выглядеть так:
  * `SELECT 100 * ROUND(X / Y, 2)`
  * `X = SELECT SUM(salary) FROM TOP10`
  * `TOP10 = SELECT SUM(salary) FROM salaries ORDER BY salary DESC LIMIT 0.1 * TOTAL` 
  * `TOTAL = SELECT COUNT(salary) FROM salaries`
  * и так далее.

### Что оценивается
* Для получения количества, суммы или среднего арифметического используются соответствующие SQL-выражения.
* Ответ на задачу 4 имеет процентный формат с округлением до двух знаков после запятой.

## Задача 5. Быстрая вставка
### Что нужно сделать
Отвлечёмся от баз данных и решим задачу на программирование.

Подобные задачи часто встречаются на собеседованиях, поэтому есть смысл иногда практиковаться в их решении. 

Реализуйте функцию `find_insert_position`, которая принимает на вход отсортированный по неубыванию массив чисел и некое число `X`, а возвращает индекс, показывающий, на какое место нужно вставить число `X`, чтобы массив остался отсортированным.

#### Пример

```python
from typing import Union
Number = Union[int, float, complex]

A: list[Number] = [1, 2, 3, 3, 3, 5]
x: Number = 4
insert_position: int = find_insert_position(A, x)
assert insert_position == 5
```

и действительно:

```python
A: list[Number] = [1, 2, 3, 3, 3, 5]
x: Number = 4
A.insert(insert_position, x)
assert A == sorted(A)
```

Запрещается использовать сторонние модули.

### Советы и рекомендации
Не забудьте учесть крайние случаи:

* Пустой массив.
* X нужно вставить первым элементом.
* X нужно вставить последним элементом.

### Что оценивается
* Решение работает за O(logN). О том, что такое «O большое», можно почитать в материалах [Big O](https://habr.com/ru/post/444594/) и [«Сложность алгоритмов. Big O. Основы»](https://bimlibik.github.io/posts/complexity-of-algorithms/).
* Функция не вставляет элемент, а только возвращает индекс.


## Общие советы и рекомендации
* Минимизируйте количество запросов и обработки результата в коде. Используйте максимум возможностей SQL. Это в разы повысит производительность:

  | Код                                                                                                                                                                       | Время работы |
  |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
  | _cursor.execute('SELECT salary FROM salaries')<br>cursor.row_factory = lambda cursor, row: row[0]<br>salaries = cursor.fetchall()<br>avg = sum(salaries) / len(salaries)_ | 27.2 ms      |
  | _cursor.execute('SELECT SUM(salary), COUNT(salary) FROM salaries')<br>sum, count = cursor.fetchone()<br>avg = sum / count_                                                | 4.18 ms      |
  | _cursor.execute('SELECT AVG(salary) FROM salaries')<br>avg = cursor.fetchone()_                                                                                           | 3.19 ms      |
* Список основных функций SQL можно найти здесь:
  * [Скалярные функции](https://www.sqlite.org/lang_corefunc.html)
  * [Агрегирующие функции](https://www.sqlite.org/lang_aggfunc.html#aggfunclist)
  * [Математические функции](https://www.sqlite.org/lang_mathfunc.html)

## Что оценивается в практической работе
* Названия переменных, функций и классов имеют значащие имена.
* При работе с БД из IDE используются сортировка и фильтрация, а также Query Console по необходимости.
* При работе с БД из Python:
  * для подключения к БД используется конструкция `try-finally-close` или контекстный менеджер;
  * для получения количества, суммы или среднего арифметического используются соответствующие
  SQL-выражения;
  * для получения одной строки используется `fetchone()`.