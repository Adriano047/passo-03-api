from flask import Flask, jsonify
app = Flask(__name__)

TASKS = [
    {"id": 1, "title": "Task 1", "description": "Description for Task 1"},
    {"id": 2, "title": "Task 2", "description": "Description for Task 2"},
]
    
@app.get("/")
def index():
    return jsonify(TASKS)

if __name__ == "__main__":
    app.run(debug=True)