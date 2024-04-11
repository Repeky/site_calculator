from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Возвращаем index.html
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    number1 = data.get('number1')
    number2 = data.get('number2')
    operation = data.get('operation')

    try:
        number1 = float(number1)
        number2 = float(number2)
        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            if number2 == 0:
                return jsonify({'result': 'Ошибка: Деление на ноль'})
            result = number1 / number2
        else:
            return jsonify({'result': 'Неизвестная операция'}), 400
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'result': 'Некорректный ввод'}), 400


if __name__ == '__main__':
    app.run(debug=True)
