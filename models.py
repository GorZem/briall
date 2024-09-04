from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    metal = db.Column(db.String(50))
    type = db.Column(db.String(50))
    # images = db.relationship('ProductImage', backref='product', lazy=True)


# class ProductImage(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     image_path = db.Column(db.String(200), nullable=False)