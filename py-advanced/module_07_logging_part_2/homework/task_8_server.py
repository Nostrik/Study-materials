from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


app = Flask(__name__)


class GetMsgForm(FlaskForm):
    msg = StringField(validators=[InputRequired()])


@app.route("/log-entry", methods=["POST"])
def accept_log_entry():
    form = GetMsgForm()

    if form.validate_on_submit():
        message = form.msg.data,
        with open('task_8_log_ser.log', mode='a') as file:
            file.write(f'{message} \n')
        return f'{message}', 200
    return 'Cannot process form', 400


@app.route("/query-example")
def query_example():
    return "Query example"


@app.errorhandler(Exception)
def handle_exception(e: Exception):
    return 'Internal server error', 500


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
    # logging.basicConfig(level=logging.debug(), filename='task_8_log_ser.log')
    #  curl -X POST http://localhost:5000/log-entry --data "msg=test"
