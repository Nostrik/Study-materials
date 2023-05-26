"""
Логов бывает очень много. А иногда - ооооооооочень много.
Из-за этого люди часто пишут логи не в человекочитаемом,
    а в машиночитаемом формате, чтобы машиной их было обрабатывать быстрее.

Напишите функцию

def log(level: str, message: str) -> None:
    pass


которая будет писать лог  в файл skillbox_json_messages.log в следующем формате:
{"time": "<время>", "level": "<level>", "message": "<message>"}

сообщения должны быть отделены друг от друга символами переноса строки.
Обратите внимание: наше залогированное сообщение должно быть валидной json строкой.

Как это сделать? Возможно метод json.dumps поможет вам?
"""
import json
import logging
import time


logger = logging.getLogger()


def log(level: str, message: str) -> None:
    data = {'time': time.ctime()[11:19], 'level': level, 'message': message}
    json_data = json.dumps(data)
    logger.info(json_data)
    pass


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        filename="skillbox_json_messages.log"
    )
    log(level='DEBUG', message='App is run')
