import os
from flask import Flask, render_template, jsonify, request

app_root = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(app_root, '..', 'templates')
static_dir = os.path.join(app_root, '..', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# In-memory store for recent orders
recent_orders = [
    {"order_id": "101", "item": "Keyboard", "quantity": 1},
    {"order_id": "102", "item": "Mouse", "quantity": 2},
    {"order_id": "103", "item": "Monitor", "quantity": 1}
]

@app.route('/')
def home():
    appname = "Vexel-app"
    return render_template("index.html", appname=appname, recent_orders=recent_orders)

@app.route('/order', methods=['POST'])
def process_order():
    order = request.json
    required_fields = ["order_id", "item", "quantity"]
    for field in required_fields:
        if field not in order:
            return jsonify({"error": f"Missing field {field}"}), 400
    if not isinstance(order["quantity"], int) or order["quantity"] <= 0:
        return jsonify({"error": "Quantity must be positive integer"}), 400

    recent_orders.append(order)
    if len(recent_orders) > 10:
        recent_orders.pop(0)

    return jsonify({"status": "success", "order_id": order["order_id"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
