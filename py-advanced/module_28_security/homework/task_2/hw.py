HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  {user_input}
</body>
</html>
"""

from flask import Flask, render_template, request, Response
from loguru import logger

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form_handler():
    logger.debug(request.headers)
    if request.method == 'POST':
        message = request.form['msg']
        logger.debug(f'message input is {message}')
        return message
    return render_template('index.html')


@app.after_request
def add_csp(response: Response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; style-src 'self' 'unsafe-inline';"
    return response


if __name__ == '__main__':
    app.run(debug=True)

# <script>alert("hack")</script>
