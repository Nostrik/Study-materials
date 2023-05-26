from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

app = Flask(__name__)


class WorkerForm(FlaskForm):
    message = StringField(validators=[InputRequired()])


@app.route("/set_log_info", methods=["POST"])
def _set_log_info():
    form = WorkerForm()

    if form.validate_on_submit():
        message = form.message.data,
        with open('log.log', mode='a') as f:
            f.write(f'{message[0]} \n')
        return "Message wrote", 200

    return "Cannot process form", 400


@app.errorhandler(Exception)
def handle_exception(e: Exception):
    return "Internal server error", 500


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
