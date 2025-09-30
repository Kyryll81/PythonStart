from os import environ, getenv

from flask import Flask, render_template, redirect, url_for, request, flash

from dotenv import load_dotenv

from form import ProductForm
from db import list_products, add_product

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = environ["FLASK_SECRET_KEY"]


@app.get('/')
def list_products_view():
    title: str = 'Products'
    products: list = list_products()
    return render_template('index.html', title=title, products=products)


@app.route('/add', methods=['GET', 'POST'])
def add_product_view():
    title: str = 'Add product'
    form = ProductForm()
    
    if form.validate_on_submit():
        product: tuple = (
            max(map(lambda l: l[0], list_products())) + 1, 
            request.form['name'], 
            request.form['price'], 
            request.form['stock']
            )
        add_product(product)
        flash("Product successfully added!", "success")
        return redirect(url_for('list_products_view'))
    return render_template('form.html', title=title, form=form)
