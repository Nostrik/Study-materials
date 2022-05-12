"""
Давайте немного вспомним Linux command line утилиты.

Напишите Flask GET endpoint, который на вход принимает флаги командной строки,
    а возвращает результат запуска команды PS с этими флагами.
    Чтобы красиво отформатировать результат вызова программы - заключите его в тэг <pre>:
        <pre>Put your text here</pre>

Endpoint должен быть по url = /ps и принимать входные значение через аргумент arg
Напомню, вызвать программу ps можно, например, вот так

    >>> import shlex, subprocess
    >>> command_str = f"ps aux"
    >>> command = shlex.split(command_str)
    >>> result = subprocess.run(command, capture_output=True)
"""
import shlex
import string
import subprocess
from typing import List
from flask import Flask, request

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def _ps():
    arguments: List[str] = request.args.getlist("arg")
    arguments_cleaned = [shlex.quote(s) for s in arguments]
    command_str = f"ps {' '.join(arguments_cleaned)}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)

    if result.returncode != 0:
        return "Something went wrong", 500

    output = result.stdout.decode()
    return string.Template(f"<pre>${output}</pre>").substitute(output=output)


if __name__ == "__main__":
    app.run(debug=True)
