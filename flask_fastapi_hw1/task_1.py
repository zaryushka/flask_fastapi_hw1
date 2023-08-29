# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!".

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!!!=)'

if __name__ == '__main__':
    app.run(debug=True)

# flask --app flask_fastapi_hw1/task_1 run --debug