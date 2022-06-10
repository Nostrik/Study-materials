from flask import Flask, request


app = Flask(__name__)


@app.route("/log-entry", methods=["POST"])
def accept_log_entry():
    msg = request.form.getlist
    print(msg)
    return f'you test msg is {msg}'


if __name__ == '__main__':
    app.run(debug=True)
#  https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-ru
