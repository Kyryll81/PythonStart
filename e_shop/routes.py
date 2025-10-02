from flask import render_template, redirect, url_for, request, flash
from form import ProductForm
from db import Product, db


def init_routes(app, db):
    @app.get('/')
    def list_products_view():
        title: str = 'Products'
        products: list[Product] = Product.query.all()
        return render_template('index.html', title=title, products=products)


    @app.route('/add', methods=['GET', 'POST'])
    def add_product_view():
        title: str = 'Add product'
        form = ProductForm()

        if form.validate_on_submit():
            product: Product = Product( 
                name=request.form['name'], 
                price=request.form['price'], 
                stock=request.form['stock']
                )
            db.session.add(product)
            db.session.commit()
            flash("Product successfully added!", "success")
            return redirect(url_for('list_products_view'))
        return render_template('form.html', title=title, form=form)
