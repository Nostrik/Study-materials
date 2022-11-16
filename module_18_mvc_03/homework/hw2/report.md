### Результаты запуска классов клиентов с методом Sessions и без него:

С методом sessions:
```DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 127.0.0.1:5000
DEBUG:urllib3.connectionpool:http://127.0.0.1:5000 "GET /api/books HTTP/1.1" 200 311
DEBUG:urllib3.connectionpool:http://127.0.0.1:5000 "GET /api/authors HTTP/1.1" 200 199
.
.
.
INFO:[clients]:Ended in 0.08399820327758789
```
Без метода sessions:
```DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 127.0.0.1:5000
DEBUG:urllib3.connectionpool:http://127.0.0.1:5000 "GET /api/books HTTP/1.1" 200 311
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 127.0.0.1:5000
DEBUG:urllib3.connectionpool:http://127.0.0.1:5000 "GET /api/authors HTTP/1.1" 200 199
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 127.0.0.1:5000
.
.
.
INFO:[clients]:Ended in 0.20099878311157227
```
Очевидно что, скорость установки HTTP соединения, в случае использования метода sessions, дает прирост в скорости.
