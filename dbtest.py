from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import inspect
from sqlalchemy import text
import request

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///identifier.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
#
# with app.app_context():
#     db.create_all()

#
# class Products2(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.Text)
#     metal = db.Column(db.Text)
#     type = db.Column(db.Text)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

with app.app_context():
    db.create_all()


with app.app_context():
    inspector = inspect(db.engine)
    print("tables=", inspector.get_table_names())
    # products = db.session.execute(text('SELECT * FROM products2')).fetchall()
    # print("products=",products)
    # for product in products:
    #     print("prod=",product)


def user_list():
    with app.app_context():
        users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return users


def user_create():
    with app.app_context():
        u = input()
        em = input()
        user = User(
                username=u,
                email=em,
            )
        db.session.add(user)
        db.session.commit()
    return "done"

def user_detail(id):
    with app.app_context():
        user = db.session.execute(db.select(id).scalars())
    return user

print(user_create())
print(user_detail(1))
print(user_list())