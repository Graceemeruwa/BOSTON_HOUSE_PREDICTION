# Boston House Price Prediction

![Project Image](house_image.jpg)

## Introduction

This project is a web application that aims to predict the median value of owner-occupied homes in $1000 (MEDV) using the Boston house dataset. The prediction model is built using XGBoost Regressor and trained on the provided dataset.

The main goal of this project is to provide users with a simple and intuitive interface to predict house prices based on various input features. Users can enter specific details related to the property, such as crime rate, industrial areas, nitric oxides concentration, number of rooms, age of the property, and more. The web application then utilizes the trained XGBoost model to predict the estimated price range for the house.

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/Graceemeruwa/BOSTON_HOUSE_PREDICTION.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run price_prediction_app.py`

## Features

- **Input Features**: The user can input various features related to crime rate, industrial areas, nitric oxides concentration, number of rooms, age of the property, and more.

- **Feature Description**: The sidebar provides the option to view the description of each input feature to help the user understand its meaning and importance.

- **Prediction**: After entering the desired input features, the user can click the "Show predicted price" button to see the predicted price range for the house.

- **Make Another Prediction**: The app also includes a "Make another prediction" button that allows the user to clear all the input fields and make a new prediction.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- XGBoost

## Dataset

The Boston house dataset used for training the prediction model can be found on (kaggle.com). It contains various features related to housing in Boston.

## Model

The prediction model is built using XGBoost Regressor from the XGBoost library. The trained model is saved as `price_pred_model.sav`.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request.

## License

None
