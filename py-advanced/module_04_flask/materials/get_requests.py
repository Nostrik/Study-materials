from typing import List, Optional
import random
from flask import Flask, request

app = Flask(__name__)


def mul(list_numbers: list) -> int:
    result = 1
    for element in list_numbers:
        result *= element
    return result


@app.route(
    "/search/", methods=["GET"],
)
def search():
    cell_tower_ids: List[int] = request.args.getlist("cell_tower_id", type=int)

    if not cell_tower_ids:
        return f"You must specify at least one cell_tower_id", 400

    phone_prefixes: List[str] = request.args.getlist("phone_prefix")

    protocols: List[str] = request.args.getlist("protocol")

    signal_level: Optional[float] = request.args.get(
        "signal_level", type=float, default=None
    )

    return (
        f"Search for {cell_tower_ids} cell towers. Search criteria: "
        f"phone_prefixes={phone_prefixes}, "
        f"protocols={protocols}, "
        f"signal_level={signal_level}"
    )


@app.route(
    "/numbers/", methods=["GET"]
)
def sum_numbers():
    list_numbers: List[int] = request.args.getlist('number')

    if not list_numbers:
        return f'kek', 400
    int_list = list(map(int, list_numbers))
    return (
        f'numbers is {list_numbers}: '
        f'sum is {sum(int_list)}, '
        f'multiplication is {mul(int_list)}'
    )


@app.route(
    "/numbersAB/", methods=["GET"]
)
def to_do_list_numbers():
    list_numbers_1: List[int] = request.args.getlist('number1')
    list_numbers_2: List[int] = request.args.getlist('number2')

    if not list_numbers_1 or not list_numbers_2:
        return f'Please check the data in URL, kek', 400
    new_list = (random.choice(list_numbers_1), random.choice(list_numbers_2))
    return (
        f'first list is {list_numbers_1} '
        f'second list is {list_numbers_2} '
        f'random of lists {new_list}'
    )


if __name__ == "__main__":
    app.run(debug=True)
