# MLB Potential Predictor

## Project Overview
This project predicts a prospect's MLB potential using logistic regression by analyzing performance metrics such as hit distance, exit velocity, and launch angle.

## Installation & Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/bp782/MLB-Potential-Predictor.git
    cd MLB-Potential-Predictor
    ```
2. Install required libraries:
    ```bash
    pip install -r requirements.txt
    ```
3. Load the model and make predictions:
    ```python
    import joblib
    import pandas as pd

    # Load the model
    model = joblib.load('src/logistic_regression_model_final.pkl')

    # Sample data with feature names
    feature_names = ['HitDistance', 'ExitVelocity', 'LaunchAngle']
    sample_data = pd.DataFrame([[0.5, 1.2, 3.4]], columns=feature_names)

    # Make a prediction
    prediction = model.predict(sample_data)
    print("Prediction:", prediction)
    ```

## Usage
- Provide instructions on how to use the project.

## License
- Include the open-source license for your project.# MLB-Potential-Predictor
