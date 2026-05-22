from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (list of objects)
items = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000
    },
    {
        "id": 2,
        "name": "Phone",
        "price": 20000
    }
]


# Helper function
def find_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return None


# CREATE
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()

    new_item = {
        "id": len(items) + 1,
        "name": data["name"],
        "price": data["price"]
    }

    items.append(new_item)

    return jsonify({
        "message": "Item created",
        "item": new_item
    }), 201


# READ ALL
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)


# READ ONE
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = find_item(item_id)

    if not item:
        return jsonify({
            "error": "Item not found"
        }), 404

    return jsonify(item)


# UPDATE
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = find_item(item_id)

    if not item:
        return jsonify({
            "error": "Item not found"
        }), 404

    data = request.get_json()

    item["name"] = data.get("name", item["name"])
    item["price"] = data.get("price", item["price"])

    return jsonify({
        "message": "Item updated",
        "item": item
    })


# DELETE
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = find_item(item_id)

    if not item:
        return jsonify({
            "error": "Item not found"
        }), 404

    items.remove(item)

    return jsonify({
        "message": "Item deleted"
    })


if __name__ == "__main__":
    app.run(debug=True)