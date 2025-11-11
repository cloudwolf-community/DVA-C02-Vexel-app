from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    # Render the HTML welcome page, using Flask’s built-in template engine
    return render_template("index.html", appname="Vexel-app")

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
    return app.send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
