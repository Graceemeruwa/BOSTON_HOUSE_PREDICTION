import streamlit as st
import pandas as pd

def DISPLAY_FEATURE_DESCRIPTION(feature):
    if feature == 'CRIM':
        st.sidebar.write('Per capita crime rate by town')
    elif feature == 'INDUS':
        st.sidebar.write("Proportion of non-retail business acres per town")
    elif feature == 'NOX':
        st.sidebar.write("Nitric oxides concentration (parts per 10 million)")
    elif feature == 'RM':
        st.sidebar.write("Average number of rooms per dwelling")
    elif feature == 'AGE':
        st.sidebar.write("Proportion of owner-occupied units built prior to 1940")
    elif feature == 'DIS':
        st.sidebar.write("Weighted distances to five Boston employment centers")
    elif feature == 'TAX':
        st.sidebar.write("Full-value property tax rate per $10,000")
    elif feature == 'PTRATIO':
        st.sidebar.write("Pupil-teacher ratio by town")
    elif feature == 'LSTAT':
        st.sidebar.write("% lower status of the population")

def load_data():
    data = pd.read_csv('boston_housing.csv')
    return data
