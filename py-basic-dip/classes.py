class User:

    def __init__(self):
        self.name = None
        self.city = None
        self.sort = None
        self.max_price = None
        self.min_price = None
        self.min_distance = None
        self.max_distance = None
        self.need_photo = None
        self.quantity_photos = None
        self.quantity_hotels = None
        self.hotels_list = []
        self.command = None
        self.date = None

    def __str__(self):
        return f'\n======================\n' \
               f'date - {self.date}\n' \
               f'user_name - {self.name}\n' \
               f'command - {self.command}\n' \
               f'city - {self.city}\n' \
               f'max_price - {self.max_price}\n' \
               f'min_price - {self.min_price}\n' \
               f'min_distance - {self.min_distance}\n' \
               f'max_distance - {self.max_distance}\n' \
               f'quantity hotels - {self.quantity_hotels}\n' \
               f'photo - {self.need_photo}\n' \
               f'======================='

    def set_name(self, name):
        """Сеттер для имени пользователя"""
        self.name = name

    def set_sort(self, order):
        """Сеттер для ордера сортировки"""
        self.sort = order

    def set_datetime(self, date):
        """Сеттер для даты и времени"""
        self.date = date

    def choice_command(self, command):
        """Сеттер для комманды, выбранной пользователем"""
        self.command = command

    def set_city(self, city):
        """Сеттер для названия города"""
        self.city = city

    def set_price(self, min_price, max_price):
        """Сеттер для устрановки минимальной и максимальной цен"""
        self.min_price = min_price
        self.max_price = max_price

    def set_quantity_hotels(self, quantity):
        """Сеттер для количества отелей"""
        self.quantity_hotels = quantity

    def set_photo(self, choice):
        """Сеттер для выбора необходимости загрузки фотографий"""
        self.need_photo = choice

    def set_quantity_photos(self, quantity):
        """Сеттер для выбора количества фото"""
        self.quantity_photos = quantity

    def set_distance(self, min_dist, max_dist):
        """Сеттер для установки минимальной и максимальной дистанций"""
        self.min_distance = min_dist
        self.max_distance = max_dist

    def get_name(self) -> str:
        """Геттер для имени пользователя"""
        return self.name

    def get_date(self) -> str:
        """Геттер для даты"""
        return self.date

    def get_sort(self) -> str:
        """Геттер для ордера сортировки"""
        return self.sort

    def get_city(self) -> str:
        """Геттер для города поиска"""
        return self.city

    def get_quantity_hotels(self) -> str:
        """Геттер количества отелей"""
        return self.quantity_hotels

    def get_photo(self) -> str:
        """Геттер необходимости загрузки фотографий"""
        return self.need_photo

    def get_quantity_photos(self) -> str:
        """Геттер количества фотографий"""
        return self.quantity_photos

    def get_command(self) -> str:
        """Геттер команды, выбранной пользователем"""
        return self.command

    def get_price(self) -> (str, str):
        """Геттер минимальнйой и максимальной цен"""
        return self.min_price, self.max_price

    def get_distance(self) -> (str, str):
        """Геттер минимального и максимального расстояний"""
        return self.min_distance, self.max_distance


class Hotel:

    def __init__(self, city, name, address, distance_to_center, cur_price, rating, hotel_id):
        self.city = city
        self.name = name
        self.address = address
        self.distance_to_center = distance_to_center
        self.cur_price = cur_price
        self.starRating = rating
        self.hotel_id = hotel_id

    def __str__(self) -> str:
        information_ru = f'{self.city}\n{self.name}\nадрес: {self.address}\n' \
                         f'расстояние до центра: {self.distance_to_center}\n' \
                         f'рейтинг: {self.starRating}\nцена: {self.cur_price}'
        return information_ru

    def get_id(self) -> str:
        """Геттер для id отеля"""
        return self.hotel_id

    def get_info(self) -> tuple:
        """Геттер для info отеля"""
        return self.name, self.city, self.address, self.cur_price
