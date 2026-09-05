def retrieve_payment_rows(df, query):
    """Lightweight local retrieval for the transaction MVP."""
    query = str(query).lower()
    mask = df.astype(str).apply(
        lambda col: col.str.lower().str.contains(query, na=False)
    ).any(axis=1)
    return df[mask]
