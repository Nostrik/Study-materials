from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

import os
import telebot
from classes import User
import handlers

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
handler = handlers.HandLer()
user = User()