from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# POST endpoint to accept name and id
@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    name = data.get('name')
    user_id = data.get('id')
    
    # Return the provided name and id
    return jsonify({
        'name': name,
        'id': user_id
    }), 200

# GET endpoint to return the current time
@app.route('/api/time', methods=['GET'])
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return jsonify({
        'current_time': current_time
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
