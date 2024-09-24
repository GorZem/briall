from flask import Flask, render_template, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import inspect


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


class Metal_Breeds(db.Model):
    __tablename__ = 'metal_breeds'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), unique=True, nullable=False)
    translated = db.Column(db.String(200))

class Products2(db.Model):
    __tablename__ = 'products2'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    metal_id = db.Column(db.Integer, db.ForeignKey('metal_breeds.id'), nullable=False)
    metal = db.relationship('Metal_Breeds', backref=db.backref('product', lazy=True))
    type = db.Column(db.Text)
    images = db.relationship('Product_Image', backref='product', lazy=True)


class Gems_Image(db.Model):
    __tablename__ = 'gems_image'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    gem_id = db.Column(db.Integer, db.ForeignKey('gems.id'), nullable=False)


class Gems(db.Model):
    __tablename__ = 'gems'
    id = db.Column(db.Integer, primary_key=True)
    breed = db.Column(db.Text)
    category = db.Column(db.Text)
    images = db.relationship('Gems_Image', backref='gem', lazy=True)






@app.route("/")
def home():
    return render_template("main.html")

@app.route('/catalog')
def catalog():
    with app.app_context():
        inspector = inspect(db.engine)
        print("tables=", inspector.get_table_names())
        products = Products2.query.all()
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

@app.route("/catalog_gems")
def catalog_gems():
    with app.app_context():
        inspector = inspect(db.engine)
        print("tables=", inspector.get_table_names())
        gems = Gems.query.all()
        return render_template('catalog_gems.html', gems=gems)

@app.route("/catalog3")
def catalog3():
    return render_template("catalog3.html")


