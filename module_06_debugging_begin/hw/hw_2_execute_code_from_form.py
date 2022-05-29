"""
Ещё раз рассмотрим Flask endpoint, принимающий код на питоне и исполняющий его.
1. Напишите для него Flask error handler,
    который будет перехватывать OSError и писать в log файл exec.log
    соответствую ошибку с помощью logger.exception
2. Добавьте отдельный exception handler
3. Сделайте так, что в случае непустого stderr (в программе произошла ошибка)
    мы писали лог сообщение с помощью logger.error
4. Добавьте необходимые debug сообщения
5. Инициализируйте basicConfig для записи логов в stdout с указанием времени
"""

import shlex
import subprocess
import logging
import sys
from typing import Optional
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired
from werkzeug.exceptions import InternalServerError

app = Flask(__name__)
logger = logging.getLogger('execute_code_logger')


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(default=10)


def run_python_code_in_subprocess(code: str, timeout: int) -> str:
    command = f'python3 -c "{code}"'
    command = shlex.split(command)
    logger.debug(command)
    process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
    )

    outs, errs = process.communicate(timeout=timeout)

    return outs.decode()


@app.route("/run_code", methods=["POST"])
def run_code():
    form = CodeForm()
    logger.debug(form)
    if form.validate_on_submit():
        code = form.code.data
        timeout = form.timeout.data
        stdout = run_python_code_in_subprocess(code=code, timeout=timeout)
        return f"Stdout: {stdout}"
    logger.error(form.errors)
    return f"Bad request. Error = {form.errors}", 400


@app.errorhandler(InternalServerError)
def handle_exception(e: InternalServerError):
    original: Optional[Exception] = getattr(e, "original_exception", None)
    if isinstance(original, OSError):
        logger.exception('OSError)')
    logger.error('Internal sever error')
    return 'Internal sever error', 500


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        filename='exec.log',
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    app.config["WTF_CSRF_ENABLED"] = False

    app.run(debug=True)
