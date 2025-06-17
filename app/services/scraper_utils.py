def calculate_last5_metrics(ranks, distances):
    form_str = "-".join(str(x) for x in ranks)
    avg_rank = sum(ranks) / len(ranks)
    win_ratio = ranks.count(1) / len(ranks)
    speed_index = sum(distances) / len(distances)
    return {
        "form_last_5": form_str,
        "avg_rank_last_5": round(avg_rank, 2),
        "speed_index": round(speed_index, 1),
        "win_ratio_last_5": round(win_ratio, 2),
    }
