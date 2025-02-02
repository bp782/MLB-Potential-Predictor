# train_model.py
import joblib
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Example training data
X_train = pd.DataFrame({
    'ExitVelocity': [90, 100, 110],
    'HitDistance': [100, 150, 200],
    'LaunchAngle': [10, 20, 30]
})
y_train = [0, 1, 1]

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'src/logistic_regression_model_final.pkl')
