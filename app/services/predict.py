import joblib
import pandas as pd
from app.schemas.horse_stats_predict import HorseStatInput

model = joblib.load("ai_model/models/horse_model.pkl")
track_condition_enc = joblib.load("ai_model/models/track_condition_enc.pkl")
jockey_enc = joblib.load("ai_model/models/jockey_enc.pkl")
trainer_enc = joblib.load("ai_model/models/trainer_enc.pkl")

def predict_ranking(data: HorseStatInput) -> str:
    df = pd.DataFrame([{
        "distance": data.distance,
        "rank": data.rank,
        "weight": data.weight,
        "handicap_point": data.handicap_point or 0,
        "earnings": data.earnings or 0,
        "track_condition": track_condition_enc.transform([data.track_condition])[0],
        "jockey": jockey_enc.transform([data.jockey])[0],
        "trainer": trainer_enc.transform([data.trainer])[0],
        "avg_rank_last_5": data.avg_rank_last_5,
        "speed_index": data.speed_index,
        "win_ratio_last_5": data.win_ratio_last_5,
    }])

    prediction = model.predict(df)[0]

    if prediction == 1:
        return "🏆 Bu at 1.lik için güçlü bir aday."
    elif prediction == 2:
        return "🥈 Bu at 2.lik için şansı yüksek."
    elif prediction == 3:
        return "🥉 Bu at 3.lüğe oynayabilir."
    else:
        return "ℹ️ İlk 5 için mücadele edebilir."
