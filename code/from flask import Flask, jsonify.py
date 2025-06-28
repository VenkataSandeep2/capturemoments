from flask import Flask, jsonify

app = Flask(__name__)

photographers = [
    {"id": "p1", "name": "Sana Click", "skills": ["Fashion", "Events"]},
]

availability_data = {
    "p1": ["2025-06-20", "2025-06-23"],
    "p2": ["2025-06-19", "2025-06-21"]
}

@app.route('/photographers', methods=['GET'])
def get_photographers():
    return jsonify(photographers)

if __name__ == "__main__":
    app.run(debug=True)