# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/students')
def student_data():
    students = [
        {'name': 'Ivan', 'surname': 'Ivanov', 'age': 25, 'average': 4},
        {'name': 'Petr', 'surname': 'Petrov', 'age': 20, 'average': 5},
        {'name': 'Maxim', 'surname': 'Maximov', 'age': 22, 'average': 3.5},
    ]
    return render_template('students.html', students=students)



if __name__ == '__main__':
    app.run(debug=True)