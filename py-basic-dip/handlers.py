import random
import re
from api_hotels import ParserApiHotels
from loguru import logger
from classes import Hotel
from models import db, User_Data, Hotel_Data
from typing import Type

logger.add('debug.log', format='{time} {level} {message} {function}', encoding='UTF-8')
use_api = ParserApiHotels()


class HandLer:

    @staticmethod
    def request_by_city_name(query: str) -> str:
        """
        Ф-ция, отправки запроса по названию города. Использует hotels api.
        Возвращает destinationId запроса.
        """
        logger.info('CALL locations_search')
        logger.debug(query)
        answer_from_api = use_api.locations_search(query)
        if not str(answer_from_api).isdigit():
            destination = answer_from_api['suggestions'][0]['entities'][0]['destinationId']
            logger.debug(destination)
            return destination
        elif answer_from_api != 200:
            logger.warning(answer_from_api)
            raise ConnectionError

    @staticmethod
    def getting_list_of_hotels(landmarkids: str, destination_id: str, sort_order: str) -> list:
        """
        Формирование списка всех отелей в запрашиваемом городе. Использует hotels api.
        Возвращает список найденных отелей
        """
        logger.info('CALL properties_list')
        answer_from_api = use_api.properties_list(landmarkids, destinationId=destination_id,
                                                  sortOrder=sort_order)
        list_hotels = answer_from_api['data']['body']['searchResults']['results']
        if not str(answer_from_api).isdigit():
            return list_hotels
        elif answer_from_api != 200:
            logger.warning(answer_from_api)
            raise ConnectionError

    def forming_a_list_subject_to_request(self, quantity_hotels: int, list_hotels: list) -> list:
        """
        Формирование готового списка отелей с учетом данных пользователя.
        Возвращает список найденных отелей.
        """
        user_hotels = []
        count = 0
        while quantity_hotels != 0:
            try:
                hotel = Hotel(list_hotels[count]['address']['locality'], list_hotels[count]['name'],
                              list_hotels[count]['address']['streetAddress'],
                              str(self.get_distance_item(list_hotels, count)) + ' km',
                              list_hotels[count]['ratePlan']['price']['current'],
                              list_hotels[count]['starRating'], list_hotels[count]['id'])
                user_hotels.append(hotel)
                count += 1
                quantity_hotels -= 1
            except KeyError as problem:
                logger.exception(problem)
                count += 1
            except IndexError:
                return user_hotels
        return user_hotels

    @staticmethod
    def get_price_item(item: list, count: int) -> float:
        """
        Ф-ция вытаскивает значение цены отелы из списка по счетчику. Убирает сивол $ и возвращает float.
        """
        temp_value = item[count]['ratePlan']['price']['current'].split(' ')
        result = str(temp_value[0]).split(',')
        result = float(str(result[0]) + str(result[1]))
        return result

    @staticmethod
    def get_distance_item(item: list, count: int) -> float:
        """
        Ф-ция вытаскивает значение расстояния до центра города по счетчику. Убирает ненужные символы,
        переводит значение из миль в километры. И возвращает значение в формате float.
        """
        temp_value = item[count]['landmarks'][0]['distance'].split(' ')
        result = float(temp_value[0].replace(',', '.'))
        return result

    def forming_a_list_subject_to_bestdeal(self, quantity_hotels: int, list_hotels: list, max_price: str,
                                           min_price: str, min_dist='0', max_dist='10') -> list:
        """
        Формирование готового списка отелей с учетом данных пользователя. Принимает на вход значения запроса:
        количества отелей, максимальной и минимальной цены, максимального и минимального расстояния.
        Возвращает список найденных отелей.
        """
        sorted_hotels = []
        count = 0
        quantity = quantity_hotels
        while quantity != 0:
            try:
                if float(min_price) < self.get_price_item(list_hotels, count) < float(max_price) and \
                        float(min_dist) < self.get_distance_item(list_hotels, count) < float(max_dist):
                    hotel = Hotel(list_hotels[count]['address']['locality'], list_hotels[count]['name'],
                                  list_hotels[count]['address']['streetAddress'],
                                  str(self.get_distance_item(list_hotels, count)) + ' km',
                                  list_hotels[count]['ratePlan']['price']['current'],
                                  list_hotels[count]['starRating'], list_hotels[count]['id'])
                    sorted_hotels.append(hotel)
                count += 1
                quantity -= 1
            except KeyError as er:
                # logger.exception(er)
                count += 1
            except IndexError:
                return sorted_hotels
        return sorted_hotels

    @staticmethod
    def gen_photo_list(answer_from_json: dict, quantity_photos: int) -> list:
        """
        Ф-ция, которая генерирует список с фотографиями одного отеля, в количестве соответствующем
        атрибуту quantity_photos, класса User.
        """
        logger.info('START gen_photo_list')
        url_list = []
        try:
            quantity = quantity_photos
            count = 0
            while quantity != 0:
                url_list.append(str(answer_from_json['hotelImages'][count]['baseUrl'].split('_')[0] + '_b.jpg'))
                quantity -= 1
                count += random.randint(0, 10)
            return url_list
        except KeyError:
            return url_list

    def photo_request(self, quantity_photos: int, find_id: str) -> list:
        """
        Ф-ция для запроса фотографий по id отеля.
        """
        logger.info('CALL photo_request')
        answer_from_api = use_api.properties_get_hotel_photos(find_id)
        if not str(answer_from_api).isdigit():
            result = self.gen_photo_list(answer_from_api, quantity_photos)
            return result
        elif answer_from_api != 200:
            logger.warning(answer_from_api)
            raise ConnectionError

    @staticmethod
    def generate_hotel_url(hotel_id: str) -> str:
        """
        Ф-ция, которая принимает id отеля и возвращает готовую ссылку для перехода на сайт отеля.
        """
        got_url = f'https://ru.hotels.com/ho{hotel_id}/?q-rooms=1&q-room-0-adults=2&q-room-0-children=0&f-hotel-id=' \
                  f'{hotel_id}&sort-order=BEST_SELLER&WOD=3&WOE=4&MGT=1&ZSX=0&SYE=3&YGF=-1'
        return got_url

    @staticmethod
    def dash_input_control(text: str) -> bool:
        try:
            if text == re.search(r'\d*-\d*', text).group(0) and (text.split('-'))[0] < (text.split('-'))[1]:
                return True
            else:
                return False
        except Exception:
            return False

    @staticmethod
    def add_hotel_db(user_obj: Type[User_Data], element: Type[Hotel]) -> None:
        """
        Ф-ция для работы с базой данных. Создает запись отеля.
        """
        try:
            with db:
                name, city, address, price = element.get_info()
                hotel_note = Hotel_Data.create(user=user_obj, name=name, city=city, address=address, price=price)
            logger.info('hotel notes add success')
        except Exception as er:
            logger.warning('db hotel ERROR')
            logger.exception(er)

    @staticmethod
    def add_user_db(date: str, telegram_id: int, user_name: str, command: str) -> Type[User_Data]:
        """
        Ф-ция для работы с базой данных. Создает запись пользователя.
        """
        try:
            with db:
                user_note = User_Data.create(date=date, telegram_id=telegram_id, user_name=user_name, command=command)
            logger.info('user note add success')
            return user_note
        except Exception as er:
            logger.warning('db user ERROR')
            logger.exception(er)

    @staticmethod
    def clr_history():
        """
        Ф-ция для очистки истории БД.
        """
        try:
            with db:
                to_del_hotel_notes = Hotel_Data.delete()
                to_del_hotel_notes.execute()
                to_del_users_notes = User_Data.delete()
                to_del_users_notes.execute()
            logger.info('history cleared')
        except Exception as er:
            logger.warning('clr database error')
            logger.exception(er)
