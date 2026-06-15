from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load products from JSON file
DATA_FILE = os.path.join(os.path.dirname(__file__), "products.json")

def load_products():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Routine templates by skin type
ROUTINES = {
    "normal": {
        "am": [
            "Gentle cleanser",
            "Hydrating toner (alcohol-free)",
            "Vitamin C serum or Hyaluronic Acid",
            "Lightweight moisturizer",
            "Sunscreen SPF 30+"
        ],
        "pm": [
            "Gentle cleanser",
            "Treatment serum (optional)",
            "Moisturizer / night cream"
        ]
    },
    "dry": {
        "am": [
            "Cream or milk cleanser",
            "Hydrating toner (glycerin/HA)",
            "Hyaluronic Acid serum",
            "Rich moisturizer (ceramides/squalane)",
            "Hydrating sunscreen SPF 30+"
        ],
        "pm": [
            "Cream cleanser",
            "HA serum",
            "Ceramide-rich cream"
        ]
    },
    "oily": {
        "am": [
            "Salicylic acid or foam cleanser",
            "Oil-control toner (niacinamide)",
            "Niacinamide serum",
            "Oil-free gel moisturizer",
            "Matte finish sunscreen SPF 30+"
        ],
        "pm": [
            "Gentle cleanser",
            "BHA/chemical exfoliant (2% salicylic) - not daily",
            "Light gel moisturizer"
        ]
    },
    "combination": {
        "am": [
            "Gentle gel cleanser",
            "Hydrating toner (light)",
            "Niacinamide or HA serum",
            "Light lotion (cream on cheeks if dry)",
            "Lightweight sunscreen"
        ],
        "pm": [
            "Gentle cleanser",
            "Niacinamide or mild exfoliant",
            "Balanced moisturizer"
        ]
    },
    "sensitive": {
        "am": [
            "Very mild fragrance-free cleanser",
            "Calming toner (centella/panthenol)",
            "Hyaluronic Acid or centella serum",
            "Barrier repair moisturizer",
            "Mineral sunscreen (zinc oxide)"
        ],
        "pm": [
            "Very mild cleanser",
            "Centella/Ceramides",
            "Barrier cream"
        ]
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    req = request.get_json()
    if not req:
        return jsonify({"error": "Invalid request"}), 400

    skin_type = req.get("skinType", "").strip().lower()
    location = req.get("location", "").strip().lower()

    if not skin_type:
        return jsonify({"error": "skinType is required"}), 400

    products = load_products()

    # Filter products by skin type and location (case-insensitive)
    def matches(product):
        # skin type match
        p_skin_types = [s.lower() for s in product.get("skin_types", [])]
        if skin_type not in p_skin_types:
            return False

        # if user provided a location, match it to product locations (if product has none, treat as global)
        if location:
            p_locations = [l.lower() for l in product.get("locations", [])]
            # if product locations empty => assume available everywhere
            if p_locations and not any(location in loc for loc in p_locations):
                return False
        return True

    matched = [p for p in products if matches(p)]

    # If zero matches, optionally return a fallback (all products for that skin type)
    if not matched:
        matched = [p for p in products if skin_type in [s.lower() for s in p.get("skin_types", [])]]

    # Build response
    response = {
        "products": matched,
        "routine": ROUTINES.get(skin_type, ROUTINES["normal"])
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
