from datetime import date
from app.database import SessionLocal
from app.models.horse_stats import HorseStats
from app.services.scraper_utils import calculate_last5_metrics

def insert_sample_horse_with_metrics():
    session = SessionLocal()
    last_5_ranks = [2, 4, 1, 1, 3]
    last_5_distances = [1400, 1600, 1200, 1400, 1300]
    metrics = calculate_last5_metrics(last_5_ranks, last_5_distances)

    new_horse = HorseStats(
        horse_name="BULUT",
        race_date=date.today(),
        race_class="Handikap 16",
        distance=1400,
        rank=2,
        jockey="A.CELIK",
        trainer="S.SALMAN",
        weight=52.5,
        track_condition="kum",
        handicap_point=80,
        earnings=220000,
        form_last_5=metrics["form_last_5"],
        avg_rank_last_5=metrics["avg_rank_last_5"],
        speed_index=metrics["speed_index"],
        win_ratio_last_5=metrics["win_ratio_last_5"]
    )

    session.add(new_horse)
    session.commit()
    session.close()
    print("✅ Veri başarıyla eklendi!")

if __name__ == "__main__":
    insert_sample_horse_with_metrics()
