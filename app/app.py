import os
import json
import redis
from flask import Flask, render_template, jsonify, request

app_root = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(app_root, '..', 'templates')
static_dir = os.path.join(app_root, '..', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
r = redis.Redis(host='localhost', port=6379, db=0)

EXAMPLE_ORDERS = [
    {"order_id": "101", "item": "Keyboard", "quantity": 1},
    {"order_id": "102", "item": "Mouse", "quantity": 2},
    {"order_id": "103", "item": "Monitor", "quantity": 1}
]

# On empty Redis, seed example orders:
if not r.exists('recent_orders'):
    r.delete('recent_orders')
    for order in EXAMPLE_ORDERS:
        r.rpush('recent_orders', json.dumps(order))

def get_recent_orders():
    orders_data = r.lrange('recent_orders', -10, -1)
    return [json.loads(order) for order in orders_data]

@app.route('/')
def home():
    appname = "Vexel-app"
    return render_template("index.html", appname=appname, recent_orders=get_recent_orders())

@app.route('/order', methods=['POST'])
def process_order():
    order = request.json
    required_fields = ["order_id", "item", "quantity"]
    for field in required_fields:
        if field not in order:
            return jsonify({"error": f"Missing field {field}"}), 400
    if not isinstance(order["quantity"], int) or order["quantity"] <= 0:
        return jsonify({"error": "Quantity must be positive integer"}), 400
    r.rpush('recent_orders', json.dumps(order))
    r.ltrim('recent_orders', -10, -1)  # Keep at most 10 recent
    return jsonify({"status": "success", "order_id": order["order_id"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
