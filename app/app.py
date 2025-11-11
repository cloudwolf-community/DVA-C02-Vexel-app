from flask import Flask, render_template, jsonify, request
import os

app_root = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(app_root, '..', 'templates')
static_dir = os.path.join(app_root, '..', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    features = [
        "Automated deployment with AWS",
        "Static asset handling",
        "RESTful API for order processing"
    ]
    return render_template("index.html", appname="Vexel-app", features=features)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
