import pickle
import json
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
model = pickle.load(open('BNBModel.pkl', 'rb'))


@app.route('/')
def index():
    return "server works"


@app.route('/greet')
def say_hello():
    return "Hello"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # print(np.array(json.loads(data)).shape)
    prediction = model.predict(np.array([json.loads(data)]))
    output = float(prediction[0])
    return jsonify(output)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
