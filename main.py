from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello')
def hello_world():
    return jsonify(message='Hello, World!')

if __name__ == '__main__':
    app.run(debug=True)
