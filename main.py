from flask import Flask
from flask import request
import dill
import numpy as np
import os

app = Flask(__name__)


@app.route("/")
def main():
    return "<h1>Front Page</h1>"


@app.route("/predict")
def predict():
    data = request.args.get('x')
    c = request.args.get('c')
    c = c[1:-1]
    c = list(map(int, c.split(",")))

    data = data[1:-1]
    data = np.array(list(map(float, data.split(",")))).reshape(-1, 1).T
    svm_model = dill.load(open("src/model.pkl", "rb"))
    predicted = svm_model.predict(data)
    return str(predicted[0])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)