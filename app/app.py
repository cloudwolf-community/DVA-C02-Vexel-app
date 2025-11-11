from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask EC2 deployment example!"})

@app.route('/order', methods=['POST'])
def process_order():
    order = request.json
    required_fields = ["order_id", "item", "quantity"]
    for field in required_fields:
        if field not in order:
            return jsonify({"error": f"Missing field {field}"}), 400
    if not isinstance(order["quantity"], int) or order["quantity"] <= 0:
        return jsonify({"error": "Quantity must be positive integer"}), 400
    return jsonify({"status": "success", "order_id": order["order_id"]})

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
