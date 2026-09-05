import pandas as pd

REQUIRED_COLUMNS = [
    "transaction_id", "merchant_id", "customer_id", "amount_inr",
    "payment_method", "status", "attempts", "failure_reason",
    "timestamp", "risk_status", "recovered_amount_inr"
]

def load_transactions(source):
    if hasattr(source, "read"):
        df = pd.read_csv(source)
    else:
        df = pd.read_csv(source)

    df["amount_inr"] = pd.to_numeric(df["amount_inr"], errors="coerce").fillna(0)
    df["recovered_amount_inr"] = pd.to_numeric(
        df["recovered_amount_inr"], errors="coerce"
    ).fillna(0)
    df["attempts"] = pd.to_numeric(df["attempts"], errors="coerce").fillna(0).astype(int)
    df["status"] = df["status"].astype(str).str.upper()
    df["failure_reason"] = df["failure_reason"].fillna("").astype(str)
    df["risk_status"] = df["risk_status"].fillna("").astype(str)
    return df

def validate_transactions(df):
    return [column for column in REQUIRED_COLUMNS if column not in df.columns]
