from flask import Flask, jsonify

app = Flask(__name__)

# Пример данных заказов (можно добавить больше)
orders = [
    {
        "id": 1,
        "items": "Кола, Чипсы",
        "delivery_address": "Общежитие 5, комната 312",
        "status": "Новый"
    },
    {
        "id": 2,
        "items": "Кола",
        "delivery_address": "Общежитие 5, комната 312",
        "status": "Новый"
    },
    {
        "id": 3,
        "items": "Суп, Салат",
        "delivery_address": "Общежитие 2, комната 105",
        "status": "В обработке"  # Этот не покажется, т.к. статус не "Новый"
    },
    {
        "id": 4,
        "items": "Суп, Чипсы",
        "delivery_address": "Общежитие 5, комната 312",
        "status": "Новый"
    }
]

@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Порт 5000, можно изменить