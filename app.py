from flask import Flask, render_template, g, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import inspect
from models import db, Jewelry, Metal, Stone, JewelryStone, Image, init_db

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = b'\xaa\x8cf\x9aTqo\x86\x0e\x85\x81\xcc\xdc\xb4F7\x0cV0E`+'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:708256@localhost:7845/briall'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True

db.init_app(app)
migrate = Migrate(app, db)



@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)




# Обработчик ошибок
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# Контексты приложения и сессий
@app.before_request
def before_request():
    g.db = db.session

@app.teardown_request
def teardown_request(exception=None):
    if hasattr(g, 'db'):
        g.db.remove()



@app.route("/")
def home():
    return render_template("main.html")

def format_description(description):
    return description.replace("\\n", "<br>").replace("\n", "<br>")

@app.route('/catalog')
def catalog():
    products = g.db.query(Jewelry).all()
    for product in products:
        product.description = format_description(product.description)
    return render_template('catalog.html', products=products)

@app.route('/catalog/<int:product_id>')
def product_detail(product_id):
    product = g.db.query(Jewelry).get_or_404(product_id)
    product.description = format_description(product.description)
    return render_template('product_detail.html', product=product)



@app.route("/catalog_gems")
def catalog_gems():
    stones = g.db.query(Stone).all()
    return render_template('catalog_gems.html', stones=stones)

@app.route("/catalog3")
def catalog3():
    return render_template("inwork.html")

@app.route("/dev")
def inwork():
    return render_template("inwork.html")

@app.route("/equipment")
def about():
    return render_template("equipment_detail.html")

if __name__ == '__main__':
    with app.app_context():
        init_db()  # Инициализация базы данных
    app.run(debug=True)
