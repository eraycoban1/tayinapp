import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Dummy veriyi oku
df = pd.read_csv("ai_model/dummy_data.csv")

# Kategorik verileri encode et
track_enc = LabelEncoder()
jockey_enc = LabelEncoder()
trainer_enc = LabelEncoder()

df["track_condition"] = track_enc.fit_transform(df["track_condition"])
df["jockey"] = jockey_enc.fit_transform(df["jockey"])
df["trainer"] = trainer_enc.fit_transform(df["trainer"])

# Özellikler ve hedef
X = df[[
    "distance", "rank", "weight", "handicap_point", "earnings",
    "track_condition", "jockey", "trainer",
    "avg_rank_last_5", "speed_index", "win_ratio_last_5"
]]
y = df["placement"]

# Modeli eğit
model = RandomForestClassifier()
model.fit(X, y)

# Klasör yoksa oluştur
os.makedirs("ai_model/models", exist_ok=True)

# Model ve encoderları kaydet
joblib.dump(model, "ai_model/models/horse_model.pkl")
joblib.dump(track_enc, "ai_model/models/track_condition_enc.pkl")
joblib.dump(jockey_enc, "ai_model/models/jockey_enc.pkl")
joblib.dump(trainer_enc, "ai_model/models/trainer_enc.pkl")

print("✅ Model ve encoderlar kaydedildi.")
