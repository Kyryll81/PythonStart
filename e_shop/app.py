from os import environ, getenv

from flask import Flask

from dotenv import load_dotenv

from form import ProductForm
from config import Config


load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)


from db import list_products, add_product, Product, db
db.init_app(app)

import routes
routes.init_routes(app, db)


with app.app_context():
    db.create_all()
    pd_1 = Product(name="ESP32", price=300.0, stock=30)
    pd_2 = Product(name="ESP8266", price=50.0, stock=12)
    pd_3 = Product(name="Граната свята Анітохійська", price=99999.99, stock=3)
    pd_4 = Product(name="Грааль святий", price=1000, stock=1)
    pd_5 = Product(name="Моє почуття гумору", price=0.0, stock=0)
    db.session.add_all([pd_1, pd_2, pd_3, pd_4, pd_5])
    product = db.session.get(Product, 1)
    if product:
        product.price = 500.0
    db.session.query(Product).filter(Product.stock < 5).delete()
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True, port=5005)