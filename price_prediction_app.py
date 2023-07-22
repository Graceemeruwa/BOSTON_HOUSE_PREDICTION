import streamlit as st
import pandas as pd
import numpy as np
from feature_description import DISPLAY_FEATURE_DESCRIPTION, load_data
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVR

#adding local image
image_path = "house_image.jpg"

# Display the image with a caption
st.image(image_path, caption="My Great Asset", use_column_width=200)

# Set the header color
st.header(":red[Boston House Price Prediction]")

# Load the data
data = pd.read_csv('boston_housing.csv')

# Adding feature description to sidebar
st.sidebar.subheader("**:blue[Check features description here.]**")
st.sidebar.write('Select feature')
feature = st.sidebar.selectbox('Select feature', options=['CRIM', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX', 'PTRATIO', 'LSTAT'], label_visibility='collapsed')
if st.sidebar.button('**:red[Show feature description]**'):
    DISPLAY_FEATURE_DESCRIPTION(feature)

# Define default values for input fields
default_CRIM = 0.0
default_INDUS = 0.0
default_NOX = 0.0
default_RM = 6.0
default_AGE = 0.0
default_DIS = 0.0
default_TAX = 187.0
default_PTRATIO = 12.0
default_LSTAT = 0.0


# Setting input parameters
left_column, middle_column, right_column = st.columns(3)

CRIM = left_column.number_input('CRIM', min_value=0.000, max_value=100.000, step=0.001, value=default_CRIM)
INDUS = middle_column.number_input('INDUS', min_value=0.000, max_value=30.000, step=0.001, value=default_INDUS)
NOX = right_column.number_input('NOX', min_value=0.000, max_value=1.000, step=0.001, value=default_NOX)

RM = left_column.number_input('RM', min_value=3.000, max_value=9.000, step=0.001, value=default_RM)
AGE = middle_column.number_input('AGE', min_value=0.000, max_value=100.000, step=0.001, value=default_AGE)
DIS = right_column.number_input('DIS', min_value=0.000, max_value=13.000, step=0.001, value=default_DIS)

TAX = left_column.number_input('TAX', min_value=187.0, max_value=711.0, step=0.1, value=default_TAX)
PTRATIO = middle_column.number_input('PTRATIO', min_value=12.00, max_value=22.00, step=0.01, value=default_PTRATIO)
LSTAT = right_column.number_input('LSTAT', min_value=0.00, max_value=40.00, step=0.01, value=default_LSTAT)

# Loading the model
with open('price_pred_model.sav', 'rb') as ppm:
    model = pickle.load(ppm)

# Creating a dataframe of input features to make it 2-dimensional
input_features = {"CRIM": CRIM, "INDUS": INDUS, "NOX": NOX, "RM": RM, "AGE": AGE, "DIS": DIS, "TAX": TAX, "PTRATIO": PTRATIO, "LSTAT": LSTAT}
input_features_frame = pd.DataFrame(input_features, index=[0])

# Feature scaling
scaler = MinMaxScaler()
input_scaled = scaler.fit_transform(input_features_frame)

# Verify Input Features
st.write("**:red[Verify Input Features]**")
st.write(input_features_frame)

# Predicting
predicted_price = model.predict(input_scaled)

# Printing prediction
if st.button('Show predicted price', key='show_predicted', help='Click to see the predicted price'):
    st.subheader(f":blue[The predicted price of the house is between USD {np.round((predicted_price[0] - 2.8) * 1000)} and USD {np.round((predicted_price[0] + 2.8) * 1000)}]")

# Add a button for making another prediction
if st.button('Make another prediction', key='make_another', help='Click to make another prediction'):
    # Reset the input fields to their default values
   # Add a button for making another prediction
    CRIM = 0.0
    INDUS = 0.0
    NOX = 0.0
    RM = 6.0
    AGE = 0.0
    DIS = 0.0
    TAX = 187.0
    PTRATIO = 12.0
    LSTAT = 0.0