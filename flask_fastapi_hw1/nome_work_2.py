# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда»,
# «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base_hw_2.html')

@app.route('/index/')
def index():
    return render_template('index_hw_2.html')

@app.route('/catalog/')
def catalog():
    return render_template('catalog_hw_2.html')

@app.route('/catalog/clothes/')
def clothes():
    return render_template('clothes_hw_2.html')

@app.route('/catalog/clothes/jacket/')
def jacket():
    return render_template('jacket_hw_2.html')

@app.route('/catalog/clothes/shirt/')
def shirt():
    return render_template('shirt_hw_2.html')

@app.route('/catalog/shoes/')
def shoes():
    return render_template('shoes_hw_2.html')

@app.route('/catalog/shoes/sports_shoes/')
def sports_shoes():
    return render_template('sports_shoes_2.html')

@app.route('/catalog/shoes/boots/')
def boots():
    return render_template('boots_hw_2.html')

@app.route('/where_to_buy/')
def where_to_buy():
    return render_template('where_to_buy_hw_2.html')

@app.route('/contacts/')
def contacts():
    return render_template('contacts_hw_2.html')

if __name__ == '__main__':
    app.run(debug=True)