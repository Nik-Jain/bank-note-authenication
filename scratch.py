# import evalml
# import pandas as pd
# from evalml.automl import AutoMLSearch

# from CONSTANTS import *

# df = pd.read_csv(INPUT)
# X = df.iloc[:, :-1]
# Y = df.iloc[:,-1]

# x_train, x_test, y_train, y_test = evalml.preprocessing.split_data(X, Y, problem_type='binary')

# automl = AutoMLSearch(X_train=x_train, y_train=y_train, problem_type='binary')
# automl.search()

# print(automl.rankings)

# pipeline = automl.best_pipeline
# print(pipeline)
# pipeline.predict(X_test)

# import streamlit as st

# option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))

import pickle
import streamlit as st
import pandas as pd

from CONSTANTS import MODEL_PATH

global input_type


classifier = ''
with open(MODEL_PATH, 'rb') as fp:
    classifier = pickle.load(fp)
print()
# print(classifier.predict([[0,0,0,0]]))

# def print_test(data):
#     st.text(f"Printing Test {data}")

# st.button('Test', on_click=print_test, kwargs={"data":"Nikhil"})
