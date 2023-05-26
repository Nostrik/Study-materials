import os
import datetime
from requests.exceptions import ConnectTimeout
from telebot import telebot, types
from loader import user, handler
from models import db, User_Data, Hotel_Data
from typing import Any
from loguru import logger
from pprint import pformat


logger.add('debug.log', format='{time} {level} {message} {function}', encoding='UTF-8')
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

try:
    with db:
        db.create_tables([User_Data, Hotel_Data])
    logger.info('Create DataModel DONE')
except Exception as db_er:
    logger.warning('Database not connect')
    logger.exception(db_er)


@bot.message_handler(commands=['start'])
def start_message(message):
    """
    Функция приветствия пользователя. Предлагает ввести имя.
    """
    bot.send_message(message.from_user.id, 'Я электронный помощник по поиску отелей\n'
                                           'агенства Easy Too Travel.\n'
                                           'Представьтесь, пожалуйста..')
    logger.info('user input start')
    bot.register_next_step_handler(message, get_user_name)


@bot.message_handler(commands=['help'])
def get_user_name(message):
    """
    Функция, которая предлагает ввести команду /help, для дальнейшей работы.
    """
    text_commands = f'/help — помощь по командам бота\n' \
                    f'/lowprice — вывод самых дешёвых отелей в городе\n' \
                    f'/highprice — вывод самых дорогих отелей в городе\n' \
                    f'/bestdeal — вывод отелей, наиболее подходящих по цене и ' \
                    f'расположению от центра\n' \
                    f'/history'
    if user.get_name() is None:
        user.set_name(message.text)
        bot.send_message(message.from_user.id, f'Привет, {user.get_name()}\n')
    bot.send_message(message.from_user.id, text_commands)


@bot.message_handler(commands=['low', 'hig', 'best', 'hist', 'lowprice', 'highprice', 'bestdeal', 'history'])
def choice_message(message):
    """
    Функция обработки нажатия основных комманд.
    """
    user.set_datetime(datetime.datetime.now())
    if message.text == '/low' or message.text == '/lowprice':
        bot.send_message(message.from_user.id, 'Выбрана команда /lowprice')
        user.choice_command('/lowprice')
        user.set_sort('PRICE')
        user_city(message)
    elif message.text == '/hig' or message.text == '/highprice':
        bot.send_message(message.from_user.id, 'Выбрана команда /highprice')
        user.choice_command('/highprice')
        user.set_sort('PRICE_HIGHEST_FIRST')
        user_city(message)
    elif message.text == '/best' or message.text == '/bestdeal':
        bot.send_message(message.from_user.id, 'Выбрана команда /bestdeal')
        user.choice_command('/bestdeal')
        user.set_sort('DISTANCE_FROM_LANDMARK')
        user_city(message)
    elif message.text == '/hist' or message.text == '/history':
        get_history(message)


@bot.message_handler(commands=['clrhist'])
def clear_history(message):
    """Функция для очистки истории поиска"""
    handler.clr_history()
    bot.send_message(message.chat.id, '- история очищена -')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    """
    Ф-ция обработки нажания кнопок Yes/No:
    """
    bot.answer_callback_query(callback_query_id=call.id)
    if call.data == 'YES':
        user.set_photo('Yes')
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        ask_quantity_photo(call.message)
    elif call.data == 'NO':
        user.set_photo('No')
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        search_fnc(call.message)
    elif call.data in ('1', '2', '3', '4', '5'):
        user.set_quantity_photos(call.data)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        search_fnc(call.message)


@bot.message_handler(content_types=['text'])
def er_message(message):
    """
    Ф-ция перехвата ввода случайного значения, введеного пользователем.
    """
    bot.send_message(message.from_user.id, 'Команда не существует, наберите /start или /help')


@logger.catch
def user_city(message):
    """
    Ф-ция запроса города. И выбора следующего шага исходя из выбранной команды.
    """
    bot.send_message(message.from_user.id, 'Введите название города: ')
    if user.get_command() != '/bestdeal':
        bot.register_next_step_handler(message, user_hotel)
    elif user.get_command() == '/bestdeal':
        bot.register_next_step_handler(message, price_range)


def price_range(message):
    """
    Ф-ция запроса диапазона цен. И перехвата значения города.
    """
    user.set_city(message.text)
    bot.send_message(message.chat.id, 'Введите диапазон цен через "-"')
    bot.register_next_step_handler(message, distance_range)


def distance_range(message):
    """
    Ф-ция запроса диапазона расстояния. И перехвата значений диапазона цен.
    """
    if handler.dash_input_control(message.text):
        user_answer = str(message.text).split('-')
        user.set_price(user_answer[0], user_answer[1])
        bot.send_message(message.chat.id, 'Введите диапазон расстояния через "-"')
        bot.register_next_step_handler(message, best_finish)
    else:
        logger.info('price input error')
        bot.send_message(message.chat.id, '- диапазон цен введен некорректно -')
        bot.register_next_step_handler(message, distance_range)


def best_finish(message):
    """
    Ф-ция перехвата значений диапазона расстояний.
    """
    if handler.dash_input_control(message.text):
        user_answer = str(message.text).split('-')
        user.set_distance(user_answer[0], user_answer[1])
        user_hotel(message)
    else:
        logger.info('distance input error')
        bot.send_message(message.chat.id, '- диапазон расстояний введен некорректно -')
        bot.register_next_step_handler(message, best_finish)


def user_hotel(message):
    """
    Ф-ция запроса количества отелей. И перехвата значения города, при выборе команды bestdeal.
    """
    if user.get_command() != '/bestdeal':
        user.set_city(message.text)
    bot.send_message(message.from_user.id, 'Введите кол-во отелей(максимум - 10) :')
    bot.register_next_step_handler(message, photo_fnc)


def photo_fnc(message):
    """
    Ф-ция для вывода клавиатуры для запроса необходимости вывода фотографий.
    """
    if message.text.isdigit() and int(message.text) <= 10:
        user.set_quantity_hotels(message.text)
        keyboard = types.InlineKeyboardMarkup()
        yes_btn = types.InlineKeyboardButton(text='Yes', callback_data='YES')
        no_btn = types.InlineKeyboardButton(text='No', callback_data='NO')
        keyboard.add(yes_btn, no_btn)
        bot.send_message(message.from_user.id, text='Нужны ли фотографии?..Y/N', reply_markup=keyboard)
    else:
        logger.info('quantity hotels error')
        bot.send_message(message.chat.id, '- количество отелей введено некорректно -')
        bot.register_next_step_handler(message, photo_fnc)


@logger.catch
def ask_quantity_photo(message):
    """
    Ф-ция для вывода клавиатуры для запроса количества фотографий.
    """
    keyboard_q_photo = types.InlineKeyboardMarkup()
    one_btn = types.InlineKeyboardButton(text='1', callback_data='1')
    two_btn = types.InlineKeyboardButton(text='2', callback_data='2')
    three_btn = types.InlineKeyboardButton(text='3', callback_data='3')
    four_btn = types.InlineKeyboardButton(text='4', callback_data='4')
    five_btn = types.InlineKeyboardButton(text='5', callback_data='5')
    keyboard_q_photo.add(one_btn, two_btn, three_btn, four_btn, five_btn)
    bot.send_message(message.chat.id, text='Количество фотографий?..1-5', reply_markup=keyboard_q_photo)


@logger.catch
def search_fnc(message):
    """
    Ф-ция начала поиска. Выводит сообщение о начале поиска и происходит переход к ф-ции для работы с API.
    """
    bot.send_message(message.chat.id, 'Выполняю поиск....')
    logger.info('user input end')
    logger.info('start of request')
    location = user.get_city()
    logger.debug(location)
    formation_of_requests(message, location)


@logger.catch
def get_history(message) -> None:
    """
    Ф-ция обработки команды history.
    """
    bot.send_message(message.chat.id, 'Выбрана команда /history')
    try:
        with db:
            for user in User_Data.select():
                bot.send_message(message.chat.id, f'Дата запроса: {user.date} \nИмя пользователя: {user.user_name}\n'
                                                  f'Выбранная команда: {user.command}')
                for hotel in user.hotel:
                    bot.send_message(message.chat.id, f'{hotel.city}\n{hotel.name}\nАдрес: {hotel.address}\n'
                                                      f'Цена: {hotel.price}\n')
    except Exception as er:
        logger.exception(er)
        bot.send_message(message.chat.id, 'К сожалению, история запросов еще не создана.')
    finally:
        logger.info('history CALLed')


@logger.catch
def keyboard_add(message, item: Any) -> None:
    """
    Ф-ция создания инлайн кнопки "перейти" для просмотра отеля на сайте.
    """
    keyboard = types.InlineKeyboardMarkup()  # Создание клавиатуры
    btn_url = handler.generate_hotel_url(hotel_id=item.get_id())  # Вызов функции формирования url
    browse_btn = types.InlineKeyboardButton(text='- перейти -', url=btn_url)  # Создание кнопки
    keyboard.add(browse_btn)  # Добавление кнопки в клавиатуру
    bot.send_message(message.chat.id, text='Смотреть размещение:', reply_markup=keyboard)  # Вывод в чат


def input_error(message) -> None:
    bot.send_message(message.chat.id, '- некорректный ввод данных - ')


def formation_of_requests(message, query: str) -> None:
    """
    Ф-ция, которая формирует, посылает, принимает и обрабатывает запрос от API.
    """
    try:
        # Создание записи информации о пользователе в БД.
        user_db_note = handler.add_user_db(user.get_date(), message.chat.id, user.get_name(), user.get_command())

        # Отправка запроса по названию города //request_by_city_name
        destination = handler.request_by_city_name(query=query)
        logger.debug(query)

        # Формирование списка всех отлей //getting_list_of_hotels
        list_hotels = []
        user_hotels = []
        if user.get_command() != '/bestdeal':
            list_hotels = handler.getting_list_of_hotels('', destination_id=destination, sort_order=user.get_sort())

            #  Формирование списка отелей с учетом данных пользователя //forming_a_list_subject_to_request
            user_hotels = handler.forming_a_list_subject_to_request(quantity_hotels=int(user.get_quantity_hotels()),
                                                                    list_hotels=list_hotels)
        elif user.get_command() == '/bestdeal':
            logger.debug(destination)
            logger.debug(user.get_sort())
            list_hotels = handler.getting_list_of_hotels('City center', destination_id=destination,
                                                         sort_order=user.get_sort())

            #  Логирование списка всех отелей для отладки
            good_format = pformat(list_hotels, depth=5)
            # logger.debug(good_format)

            #  Формирование списка отелей с учетом данных пользователя //forming_a_list_subject_to_bestdeal
            min_price, max_price = user.get_price()
            min_dist, max_dist = user.get_distance()
            user_hotels = handler.forming_a_list_subject_to_bestdeal(quantity_hotels=int(user.get_quantity_hotels()),
                                                                     list_hotels=list_hotels, max_price=max_price,
                                                                     min_price=min_price, min_dist=min_dist,
                                                                     max_dist=max_dist)

        #  Вывод результатов поиска в чат0
        if user.get_photo() == 'Yes':
            for elem in user_hotels:
                bot.send_message(message.chat.id, elem)
                hotel_photo_answer = handler.photo_request(quantity_photos=int(user.get_quantity_photos()),
                                                           find_id=elem.get_id())
                try:
                    for i_photo in hotel_photo_answer:
                        bot.send_photo(message.chat.id, i_photo)
                except Exception as problem:
                    logger.error('photo_answer problem')
                    logger.exception(problem)
                handler.add_hotel_db(user_obj=user_db_note, element=elem)
                keyboard_add(message, item=elem)
        elif user.get_photo() == 'No':
            for elem in user_hotels:
                bot.send_message(message.chat.id, elem)
                handler.add_hotel_db(user_obj=user_db_note, element=elem)
                keyboard_add(message, item=elem)
        bot.send_message(message.chat.id, '- поиск завершен -')
        logger.debug('end')

    except ConnectTimeout as err:
        logger.exception(err)
        bot.send_message(message.chat.id, f'- превышен таймаут -\n'
                                          f'- попробуйте позже -')
    except IndexError as err:
        logger.error(err)
        bot.send_message(message.chat.id, '- город не найден -')

    except Exception as err:
        logger.exception(err)
        bot.send_message(message.chat.id, '- сервис недоступен -')


def run():
    logger.info('-START PROGRAM-')
    bot.polling(none_stop=True)


if __name__ == '__main__':
    while True:
        try:
            run()
        except Exception as ex:
            logger.warning('Connection Error')
            logger.exception(ex)
