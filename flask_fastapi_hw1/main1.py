from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def hello_world():
    colors = ['Red', 'White', 'Green']
    return render_template('index.html', colors=colors)
    # return redirect(url_for('about'))


@app.route('/about')
def about():
    return render_template('about_1.html')

html = """<p><h1>Буря мглою,<br>Небо кроет.<br>Вихри снежные крутя.<br>То как зверь она завоет,<br>То заплачет, как дитя.</h1></p>"""
poems = ['Буря мглою,', 'Небо кроет.', 'Вихри снежные крутя.', 'То как зверь она завоет,', 'То заплачет, как дитя.']

@app.route('/text/')
def text():
    # return html
    return '<h1>Стихотворение</h1>\n<p>' + '<br>'.join(poems) + '</p>'

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True)



# flask --app flask_fastapi_hw1/main1 run --debug