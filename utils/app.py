#app.py

from flask import Flask, request, jsonify, send_from_directory
from demo import run_agent, SKILLS 

# --- import your agent ---
# f the import path to match your project structure

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
    selected_skill = data.get("skill", "").strip()
    history = data.get("history", [])  # client sends history each time

    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    if not selected_skill:
        return jsonify({"error": "No skill selected"}), 400
    if selected_skill not in SKILLS and selected_skill != "auto":
        return jsonify({"error": f"Invalid skill: {selected_skill}"}), 400

    try:
        result = run_agent(user_input, skill=selected_skill, history=history)
        return jsonify(result)  # result["history"] has the updated history
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)