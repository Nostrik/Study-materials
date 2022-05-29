import json
import logging
import os
from flask import Flask


app = Flask(__name__)
logger = logging.getLogger("account_book")
current_dir = os.path.dirname(os.path.abspath(__file__))
fixtures_dir = os.path.join(current_dir, "fixtures")
departments = {"IT": "it_dept", "PROD": "production_dept"}


@app.route("/account/<department>/<int:account_number>/")
def sort_endpoint(department: str, account_number: int):
    dept_directory_name = departments.get(department)
    if dept_directory_name is None:
        return "Department not found", 404
    full_department_path = os.path.join(fixtures_dir, dept_directory_name)
    account_data_file = os.path.join(full_department_path, f"{account_number}.json")

    with open(account_data_file, "r") as fi:
        account_data_txt = fi.read()
    account_data_json = json.loads(account_data_txt)
    name, birth_date = account_data_json["name"], account_data_json["birth_date"]
    day, month, _ = birth_date.split(".")
    return f"{name} was born on {day}.{month}"


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Started account server")
    app.run(debug=True)
