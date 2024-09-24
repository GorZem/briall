from flask_sqlalchemy import SQLAlchemy
from app import app

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