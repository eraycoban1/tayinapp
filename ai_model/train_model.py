import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Veri dosyasını yükle
df = pd.read_csv("ai_model/dummy_data.csv")

# 'form_last_5' sütununu float ortalamaya çevir
def form_to_avg(form_string):
    try:
        return sum([int(x) for x in form_string.split("-")]) / 5
    except:
        return 0.0

df["form_last_5"] = df["form_last_5"].apply(form_to_avg)
# race_date sütununu sayıya çevir (örnek: timestamp formatı)
df["race_date"] = pd.to_datetime(df["race_date"]).astype(int) / 10**9  # saniye cinsinden epoch time


# Encode edilecek kategorik sütunlar
categorical_columns = ["jockey", "trainer", "track_condition", "race_class", "horse_name"]
encoders = {}

for col in categorical_columns:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])
    encoders[col] = encoder
    joblib.dump(encoder, f"ai_model/models/{col}_enc.pkl")

# Özellikler ve hedef sütun
X = df.drop(columns=["rank"])
y = df["rank"]

# Modeli eğit
model = RandomForestClassifier()
model.fit(X, y)

# Modeli kaydet
joblib.dump(model, "ai_model/models/horse_model.pkl")

print("✅ Model ve encoder'lar başarıyla kaydedildi.")
