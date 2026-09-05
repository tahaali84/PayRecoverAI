RULES = {
    "INSUFFICIENT_FUNDS": {
        "root_cause": "The customer's available balance is insufficient for the transaction.",
        "evidence": "Failure reason is INSUFFICIENT_FUNDS.",
        "action": "Send a payment reminder and suggest retrying later or using another payment method.",
        "priority": "Medium",
    },
    "AUTHENTICATION_FAILED": {
        "root_cause": "The payment authentication step failed.",
        "evidence": "Failure reason is AUTHENTICATION_FAILED.",
        "action": "Ask the customer to retry authentication and provide an alternate payment method.",
        "priority": "High",
    },
    "ISSUER_DECLINED": {
        "root_cause": "The card/payment issuer declined the transaction.",
        "evidence": "Failure reason is ISSUER_DECLINED.",
        "action": "Avoid repeated retries; recommend an alternate payment method or escalation.",
        "priority": "High",
    },
    "BANK_TIMEOUT": {
        "root_cause": "The banking/payment network did not respond within the expected time.",
        "evidence": "Failure reason is BANK_TIMEOUT.",
        "action": "Retry once after a short delay; then offer an alternate method.",
        "priority": "Medium",
    },
    "NETWORK_ERROR": {
        "root_cause": "A network communication problem interrupted the payment attempt.",
        "evidence": "Failure reason is NETWORK_ERROR.",
        "action": "Retry once after a short delay and offer an alternate payment option if needed.",
        "priority": "Medium",
    },
}

def analyze_failure(transaction):
    reason = str(transaction["failure_reason"]).strip()
    return RULES.get(reason, {
        "root_cause": "The payment failed for an unclassified reason.",
        "evidence": f"Recorded failure reason: {reason or 'UNKNOWN'}.",
        "action": "Review the transaction and use an alternate payment method.",
        "priority": "Medium",
    })
