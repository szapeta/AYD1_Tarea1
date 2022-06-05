from flask_cors import CORS
from flask import Flask, request


app = Flask(__name__)
CORS(app)


@app.route('/rest', methods=['GET'])
def main():
    value1 = request.json['value1']
    value2 = request.json['value2']
    return str(value1 - value2)


if __name__ == '__main__':
    app.run(
        port=3000
    )
