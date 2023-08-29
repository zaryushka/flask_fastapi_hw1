# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    # return '<h1>Моя первая HTML страница</h1>\n<p>Привет, мир!</p>'
    return render_template('index1.html')




if __name__ == '__main__':
    app.run(debug=True)