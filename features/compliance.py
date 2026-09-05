def payment_safety_checks(transaction):
    """Simple demo guardrails for payment recovery actions."""
    attempts = int(transaction.get("attempts", 0))
    reason = str(transaction.get("failure_reason", ""))

    if attempts >= 3:
        return {
            "status": "ESCALATE",
            "message": "Multiple attempts detected. Avoid repeated retries and consider escalation or an alternate method."
        }

    if reason == "ISSUER_DECLINED":
        return {
            "status": "ESCALATE",
            "message": "Issuer decline detected. Do not repeatedly retry the same payment method."
        }

    return {
        "status": "SAFE_TO_RECOVER",
        "message": "A bounded recovery action can be considered."
    }
