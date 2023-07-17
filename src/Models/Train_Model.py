#Code to train Model Versions

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
import xgboost as xgb

#creates a scalar that can be saved and used on test data
def scale(X_train, file_path):

    # Create an instance of the scaler
    scaler = StandardScaler()

    # Fit the scaler to the training data
    scaler.fit(X_train)

    # Save the scaler to a file
    joblib.dump(scaler, file_path)

#loads scalar from file and returns scaler
def load_scale(file_path):
    # Load the saved scaler from file
    scaler = joblib.load(file_path)

    return scaler


#creates a trained model using multiple linear regression
#saves model
def multiple_linear_regression(X_train, y_train, file_path):

    



    #standardize features
    #X_train = scaler.fit_transform(X_train)

    # Create an instance of the MLR model
    model = LinearRegression()

    # Fit the model to the training data
    model.fit(X_train, y_train)

    # Save the model to a file
    joblib.dump(model, file_path)

    return model

#trains a neural network model
def neural_network(X_train, y_train, X_test, y_test, num_epochs, file_path):

    # Define the number of input features
    input_dim = len(X_train[0])

    # Create the model
    model = keras.Sequential([
        layers.Dense(9, activation='relu', input_dim=input_dim),
        layers.Dense(1, activation='linear')
    ])

    # Compile the model with MSE loss
    model.compile(optimizer='adam', loss='mse')

    # Define early stopping callback
    early_stopping = EarlyStopping(patience=30, restore_best_weights=True)

    # Train the model
    model.fit(X_train, y_train, epochs=num_epochs, batch_size=32, validation_data=(X_test, y_test), callbacks=[early_stopping])

    # Save the model to a file
    joblib.dump(model, file_path)

    return model

#trains a random forest model
def random_forest(X_train, y_train, n_estimators, file_path):

    # Create a random forest classifier
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Save the model to a file
    joblib.dump(model, file_path)

    return model

#creates a gradient boost model
def gradient_boost(X_train, y_train, n_estimators, file_path):

    # Create a Gradient Boosting classifier
    model = GradientBoostingRegressor(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Save the model to a file
    joblib.dump(model, file_path)

    return model 

#creates a xgboost model
def xgboost(X_train, y_train, n_estimators, file_path):

    # Create a Gradient Boosting classifier
    model = xgb.XGBRegressor(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Save the model to a file
    joblib.dump(model, file_path)

    return model 