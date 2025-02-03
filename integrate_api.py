import joblib
import pandas as pd

# Load the model
model = joblib.load('src/logistic_regression_model_final.pkl')  # Adjust the path as needed

# Function to predict
def predict(data):
    features = pd.DataFrame([data])
    prediction = model.predict(features)
    return {'prediction': prediction.tolist()}

# Example usage
if __name__ == "__main__":
    # Sample data for prediction
    data = {
      "ExitVelocity": 90,
      "HitDistance": 150,
      "LaunchAngle": 20
    }

    result = predict(data)
    print(result)
