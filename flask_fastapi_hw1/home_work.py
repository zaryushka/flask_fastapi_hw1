# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда»,
# «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base_hw.html')

@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')

@app.route('/clothes/jacket/')
def jacket():
    return render_template('jacket.html')

@app.route('/clothes/shirt/')
def shirt():
    return render_template('shirt.html')

@app.route('/shoes/sports_shoes/')
def sports_shoes():
    return render_template('sports_shoes.html')

@app.route('/shoes/boots/')
def boots():
    return render_template('boots.html')

@app.route('/where_to_buy/')
def where_to_buy():
    return render_template('where_to_buy.html')


if __name__ == '__main__':
    app.run(debug=True)