from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/users", methods =['GET'])
def return_get():
    output = {'payload':'success'}
    return jsonify(output)


@app.route("/user", methods =['DELETE'])
def delete_user():
    output = {
        "payload":"success"
    }
    output.clear()
    return jsonify({"payload":"success"})

@app.route("/user", methods =['PUT'])
def put_user():
    return jsonify({'payload': 'success', 'error': False})
   
@app.route('/user', methods=['POST'])
def post_user():
    return jsonify({'payload': 'success'})   

@app.route('/api/v1/users', methods=['GET'])
def get_users_v1():
    return jsonify({'payload': []})

@app.route('/api/v1/user', methods=['POST'])
def post_user_v1():
    email = request.args.get('email')
    name = request.args.get('name')
    return jsonify({'payload': {'email': email, 'name': name}})

@app.route('/api/v1/user/add', methods=['POST'])
def add_user():
    email = request.form.get('email')
    name = request.form.get('name')
    user_id = request.form.get('id')
    return jsonify({'payload': {'email': email, 'name': name, 'id': user_id}})

@app.route('/api/v1/user/add', methods=['PUT'])
def add_user():
    email = request.form.get('email')
    name = request.form.get('name')
    user_id = request.form.get('id')
    return jsonify({'payload': {'email': email, 'name': name, 'id': user_id}})

if __name__ == "__main__":
    app.run(debug=True)
