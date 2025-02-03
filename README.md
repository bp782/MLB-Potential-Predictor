# MLB Prospect Prediction

## Project Overview
This project predicts an MLB player's potential and projects their career impact based on current performance and historical data.

## How the Model Works
The model uses a logistic regression approach, trained on features like hit distance, exit velocity, and launch angle to predict the success of a prospect.

## How to Run the Model

### Running the Model Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/<bp782>/MLB-Potential-Predictor.git
   cd MLB-Potential-Predictor
   
2. Install dependencies
pip install -r requirements.txt

3. Run the model script
python integrate_api.py

4. Example usage to test predictions
import joblib
import pandas as pd

# Load the model
model = joblib.load('src/logistic_regression_model_final.pkl')

# Function to predict
def predict(data):
    features = pd.DataFrame([data])
    prediction = model.predict(features)
    return {'prediction': prediction.tolist()}

# Example usage:
data = {
  "ExitVelocity": 90,
  "HitDistance": 150,
  "LaunchAngle": 20
}

result = predict(data)
print(result)

Deployment status 

The project does not include a deployed model due to billing restrictions. However the trained logistic regression model has been integrated with the Gemini API and can be tested locally

Usage 

The code and model provided in the repository can predict the potential of MLB players based on their performance metrics  

License 

This project is licensed under the MIT License 

