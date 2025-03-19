from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Item(db.Model):
    name = db.Column(db.String(length=30))

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '123', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '1231', 'price': 622},
        {'id': 3, 'name': 'Keyboar', 'barcode': '1234', 'price': 987}
    ]
    return render_template('market.html', items = items)

if __name__ == '__main__':
    app.run(debug=True)