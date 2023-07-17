# code to make predictions on trained models

from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib

#loads model
def load_model(file_path):
    
    # Load the saved model from file
    model = joblib.load(file_path)

    return model

#makes predictions and return rmse
def predict(model, X_test, y_test):

    #standardize features
    #X_test = scaler.fit_transform(X_test)

    #gets predictions
    y_pred = model.predict(X_test)


    #converts back from log transform
    #y_pred = np.exp(y_pred)



    #Calculate rmse
    mse = mean_squared_error(y_test,y_pred)
    rmse = np.sqrt(mse)

    #prints rmse
    print("Root Mean Squared Error (RMSE):", rmse)

    return y_pred

