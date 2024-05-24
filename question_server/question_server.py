from flask import Flask, request, jsonify, abort
import json

app = Flask(__name__)

with open('assets/questions.json', 'r') as f:
    questions = json.load(f)

API_KEY = "abcd1234"

@app.route('/<api_key>/question', methods=['GET'])
def question(api_key):
    if api_key != API_KEY:
        return abort(403, description="Forbidden: Invalid API Key")

    index = request.args.get('index', type=int, default=0)

    if index < 0 or index >= len(questions):
        return abort(404, description="Not Found: Question index out of range")

    return jsonify(questions[index])

@app.route('/<api_key>/question_count', methods=['GET'])
def question_count(api_key):
    if api_key != API_KEY:
        return abort(403, description="Forbidden: Invalid API Key")

    return jsonify({"count": len(questions)})

if __name__ == '__main__':
    app.run(debug=True)
