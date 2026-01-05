from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample menu data
menu = [
    {"id": 1, "name": "Paneer Butter Masala", "price": 220},
    {"id": 2, "name": "Veg Biryani", "price": 180},
    {"id": 3, "name": "Chicken Masala", "price": 250}
]

# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Python Restaurant App"
    })

# Get full menu
@app.route("/menu", methods=["GET"])
def get_menu():
    return jsonify(menu)

# Add new dish
@app.route("/menu", methods=["POST"])
def add_dish():
    data = request.get_json()
    new_dish = {
        "id": len(menu) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    menu.append(new_dish)
    return jsonify(new_dish), 201

# Update dish price
@app.route("/menu/<int:dish_id>", methods=["PUT"])
def update_dish(dish_id):
    data = request.get_json()
    for dish in menu:
        if dish["id"] == dish_id:
            dish["price"] = data["price"]
            return jsonify(dish)
    return jsonify({"error": "Dish not found"}), 404

# Delete a dish
@app.route("/menu/<int:dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    for dish in menu:
        if dish["id"] == dish_id:
            menu.remove(dish)
            return jsonify({"message": "Dish deleted"})
    return jsonify({"error": "Dish not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
