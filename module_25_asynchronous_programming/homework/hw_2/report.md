### Report on the download time of cats on threads, processes and asynchrony:


| Quantity | Thread | Process | Async  | With blocking Open |
|----------|--------|---------|--------|--------------------|
| 10       | 4 sec  | 3 sec   | 3 sec  | 3 sec              |
| 50       | 19 sec | 10 sec  | 10 sec | 11 sec             |
| 100      | 40 sec | 32 sec  | 15s    | 15 sec             |