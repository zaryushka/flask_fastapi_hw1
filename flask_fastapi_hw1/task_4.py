# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.


from flask import Flask

app = Flask(__name__)

@app.route('/<string>')
def len_string(string):
    return f'Длина строки {string} равна {len(string)}'


if __name__ == '__main__':
    app.run(debug=True)