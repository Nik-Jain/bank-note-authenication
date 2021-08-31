import pickle

import numpy as np
import pandas as pd
from flasgger import Swagger
from flask import Flask, request

from CONSTANTS import MODEL_PATH

app = Flask(__name__)
Swagger(app)
classifier = ''
with open(MODEL_PATH, 'rb') as fp:
    classifier = pickle.load(fp)

@app.route('/')
def welcome():
    #TODO: Add docstring for Swagger
    
    return "Welcome All"

@app.route('/predict', methods=['Get'])
def predict_note_authentication():

    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')

    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    # print(prediction)

    return "Hello the answer is" + str(prediction)

@app.route('/predict_file', methods=['POST'])
def predict_note_file():
    df_test = pd.read_csv(request.files.get('file'))
    prediction = classifier.predict(df_test)

    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
