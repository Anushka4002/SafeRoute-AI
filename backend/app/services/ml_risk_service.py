import joblib
import pandas as pd
from pathlib import Path


class MLRiskService:

    def __init__(self):

        model_path = (
            Path(__file__).parent.parent
            / "ml"
            / "risk_model.pkl"
        )

        self.model = joblib.load(model_path)

    def predict_risk_multiplier(
        self,
        time_of_day="afternoon",
        weather="clear",
        speed_limit=50,
        past_incidents=1
    ):

        input_df = pd.DataFrame([{
            "time_of_day": time_of_day,
            "weather": weather,
            "speed_limit": speed_limit,
            "past_incidents": past_incidents
        }])

        prediction = self.model.predict(input_df)[0]

        return round(float(prediction), 3)