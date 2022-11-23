from sqlalchemy import Table, create_engine, MetaData, Column, Integer, String, Float, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, mapper, declarative_base
from sqlalchemy import create_engine
from flask import Flask, jsonify, abort, request

app = Flask(__name__)
engine = create_engine('sqlite:///python.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Product(Base):
    __table__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nulalble=False)
    count = Column(Integer, default=0)
    price = Column(Float, default=0)

    def __repr__(self):
        return F"Товар {self.title}, в количестве: {self.count}, цена: {self.price}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route('/')
def hello_world():
    return 'Hello_world!'


@app.route('/products', methods=['GET'])
def get_all_products():
    #  получение списка товаров на складе
    products = session.query(Product).all()
    products_list = []
    for product in products:
        products_list.append(product.to_json())
    return jsonify(products_list=products_list), 200


@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    #  получение товара по id
    product = session.query(Product).filter(Product.id == id).one_or_none()
    if product is None:
        abort(404)
    return jsonify(product=product.to_json()), 200


@app.route('/products', methods=['POST'])
def add_product():
    #  добавить новый товар на склад
    title = request.form.get('title', type=str)
    count = request.form.get('count', type=int)
    price = request.form.get('price', type=float)
    new_product = Product(
        title=title,
        count=count,
        price=price
    )
    session.add(new_product)
    session.commit()
    return 'Товар успешно создан', 201


@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    #  убрать товар со склада
    #  с помощью метода объекта Query
    session.query(Product).filter(Product.id == id).delete()
    session.commit()
    #  используя специальную конструкцию delete
    # from sqlalchemy import delete
    # query = delete(Product).where(Product.id === id)
    # session.execute(query)
    return 'Товар успешно удален', 200


@app.route('/product/<int:id>', methods=['PATCH'])
def update_product(id):
    #  Обновить товар на складе
    title = request.form.get('title', type=str)
    count = request.form.get('count', type=str)
    price = request.form.get('price', type=str)
    # 1 var update
    product = session.query(Product).filter(Product.id == id).one_or_none()
    if title:
        product.title = title
    if count:
        product.count = count
    if price:
        product.price = price
    session.commit()
    # 2 var update
    session.query(Product).filter(Product.id == id).update({
        Product.title: title,
        Product.count: count,
        Product.price: price
    })
    session.commit()
    # 3 var update
    from sqlalchemy import update
    query = update(Product).where(Product.id == id).values(
        title=title,
        count=count,
        price=price
    )
    print(query)
    session.execute(query)
    return 'Товар упешно обновлен', 200


if __name__ == '__main__':
    app.run()
