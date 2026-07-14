import pandas as pd
import numpy as np

np.random.seed(42)

TIME_OF_DAY = ["morning", "afternoon", "evening", "night"]
WEATHER = ["clear", "rainy", "foggy"]

TIME_BASE_RISK = {
    "morning": 0.15,
    "afternoon": 0.20,
    "evening": 0.35,
    "night": 0.55
}

WEATHER_BASE_RISK = {
    "clear": 0.10,
    "rainy": 0.35,
    "foggy": 0.45
}

rows = []

for _ in range(2000):

    time_of_day = np.random.choice(TIME_OF_DAY)
    weather = np.random.choice(WEATHER)
    speed_limit = np.random.choice([30, 40, 50, 60, 80])
    past_incidents = np.random.poisson(2)

    base = (
        TIME_BASE_RISK[time_of_day]
        + WEATHER_BASE_RISK[weather]
    ) / 2

    speed_factor = (speed_limit - 30) / 50 * 0.3
    incident_factor = min(past_incidents * 0.05, 0.3)

    noise = np.random.normal(0, 0.05)

    risk_multiplier = base + speed_factor + incident_factor + noise
    risk_multiplier = round(max(0.5, min(2.5, 1 + risk_multiplier * 2)), 3)

    rows.append({
        "time_of_day": time_of_day,
        "weather": weather,
        "speed_limit": speed_limit,
        "past_incidents": past_incidents,
        "risk_multiplier": risk_multiplier
    })

df = pd.DataFrame(rows)
df.to_csv("app/ml/road_risk_dataset.csv", index=False)

print("Dataset generated: app/ml/road_risk_dataset.csv")
print(df.head())