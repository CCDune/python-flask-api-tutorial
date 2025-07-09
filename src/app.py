from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
	{ "label": "make the bed", "done": True },
	{ "label": "get a new career", "done": False },
	{ "label": "learn Spanish", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text
   
    

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        del todos[position]
    return jsonify(todos)

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)