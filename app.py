from flask import Flask, render_template, g
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import inspect
from sqlalchemy import text

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


db = SQLAlchemy(app)


class Product_Image(db.Model):
    __tablename__ = 'product_image'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products2.id'), nullable=False)

class Products2(db.Model):
    __tablename__ = 'products2'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    metal = db.Column(db.Text)
    type = db.Column(db.Text)
    images = db.relationship('Product_Image', backref='product', lazy=True)







@app.route("/")
def home():
    return render_template("main.html")

@app.route('/catalog')
def catalog():
    with app.app_context():
        inspector = inspect(db.engine)
        print("tables=", inspector.get_table_names())
        products = Products2.query.all()
        print("products=",products)
        for product in products:
            print("prod=",product)
        return render_template('catalog.html', products=products)

@app.route('/catalog/<int:product_id>')
def product_detail(product_id):
    product = Products2.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/catalog/00001")
def details():
    return render_template("details.html")

@app.route("/catalog2")
def catalog2():
    return render_template("catalog2.html")

@app.route("/catalog3")
def catalog3():
    return render_template("catalog3.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)