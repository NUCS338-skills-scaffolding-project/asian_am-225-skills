from flask import Flask, request, jsonify, send_from_directory
import json
import os

# --- import your agent ---
# f the import path to match your project structure
from fullDemo import run_agent, SKILLS  # assumes agent.py is in the same folder

app = Flask(__name__, static_folder=".")


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/skills", methods=["GET"])
def list_skills():
    return jsonify({
        "skills": [
            {"name": name, "description": meta["description"]}
            for name, meta in SKILLS.items()
        ]
    })


@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    user_input = data.get("input", "").strip()

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        result = run_agent(user_input)
        return jsonify({"conversation": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)