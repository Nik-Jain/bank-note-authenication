import pickle
import streamlit as st
import pandas as pd

from CONSTANTS import MODEL_PATH

global input_type


classifier = ''
with open(MODEL_PATH, 'rb') as fp:
    classifier = pickle.load(fp)

def predict(type, data):
    if type=='raw':
        if data == [0,0,0,0]:
            st.error('Please enter values of variance, skewness, curtosis, entropy')
        else:
            st.text(f'Your predicted value: {classifier.predict([data])}')
    else:
        st.text(f'Your predicted values are {classifier.predict(data)}')

def input_pallet():
    if input_type.lower() == 'raw':
        variance = st.number_input('variance')
        skewness = st.number_input('skewness')
        curtosis = st.number_input('curtosis')
        entropy = st.number_input('entropy')
        st.button('Predict', on_click=predict, kwargs={'type':'raw', 'data':[variance, skewness, curtosis, entropy]})
        
    elif input_type.lower() == 'file':
        fp = st.file_uploader('Upload File',)
        if fp:
            df = pd.read_csv(fp)
            st.button('Predict', on_click=predict, kwargs={'type':'file', 'data':df})


input_type = st.selectbox('Select type of input',['Select input type','Raw', 'File'],index=0)
input_pallet()
