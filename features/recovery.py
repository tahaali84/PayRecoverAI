from .root_cause import analyze_failure

def build_recovery_plan(failed_df):
    rows = []
    for _, tx in failed_df.iterrows():
        rca = analyze_failure(tx)
        score = float(tx["amount_inr"]) + float(tx["attempts"]) * 500
        if rca["priority"] == "High":
            score += 1000

        rows.append({
            "transaction_id": tx["transaction_id"],
            "amount_inr": tx["amount_inr"],
            "failure_reason": tx["failure_reason"],
            "attempts": tx["attempts"],
            "priority": rca["priority"],
            "priority_score": round(score, 0),
            "recommended_action": rca["action"],
            "recovered_amount_inr": tx["recovered_amount_inr"],
        })

    return __import__("pandas").DataFrame(rows).sort_values(
        "priority_score", ascending=False
    )

def recovery_summary(df):
    failed = df[df["status"].eq("FAILED")].copy()
    summary = failed.groupby("failure_reason").agg(
        failed_transactions=("transaction_id", "count"),
        amount_at_risk=("amount_inr", "sum"),
        recovered_amount=("recovered_amount_inr", "sum"),
    ).reset_index()
    summary["recovery_rate_%"] = (
        summary["recovered_amount"] / summary["amount_at_risk"] * 100
    ).fillna(0).round(1)
    return summary
