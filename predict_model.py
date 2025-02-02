# predict_model.py
import joblib
import pandas as pd

# Load the model
model = joblib.load('src/logistic_regression_model_final.pkl')

# Sample data with feature names
feature_names = ['ExitVelocity', 'HitDistance', 'LaunchAngle']
sample_data = pd.DataFrame([[0.5, 1.2, 3.4]], columns=feature_names)

# Make a prediction
prediction = model.predict(sample_data)
print("Prediction:", prediction)
