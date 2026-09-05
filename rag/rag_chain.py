import pandas as pd

def _context(df, selected_transaction=None):
    if selected_transaction is not None:
        tx = selected_transaction
        return (
            f"Transaction {tx['transaction_id']}, amount ₹{tx['amount_inr']:,.0f}, "
            f"method {tx['payment_method']}, status {tx['status']}, attempts {tx['attempts']}, "
            f"failure reason {tx['failure_reason']}, risk {tx['risk_status']}."
        )

    failed = df[df["status"].eq("FAILED")]
    return (
        f"Dataset has {len(df)} transactions and {len(failed)} failed payments. "
        f"Failed amount at risk is ₹{failed['amount_inr'].sum():,.0f}. "
        f"Recovered amount is ₹{df['recovered_amount_inr'].sum():,.0f}."
    )

def answer_payment_question(question, df, api_key, selected_transaction=None):
    try:
        from langchain_groq import ChatGroq
        from langchain_core.messages import SystemMessage, HumanMessage

        llm = ChatGroq(
            model="qwen/qwen3.6-27b",
            temperature=0.1,
            api_key=api_key,
        )

        prompt = f"""
You are PayRecover AI, a payment revenue-recovery assistant.
Use only the supplied payment evidence. Do not invent gateway facts.
Give a concise answer and recommend bounded retries.
Evidence:
{_context(df, selected_transaction)}

Question:
{question}
"""
        result = llm.invoke([
            SystemMessage(content="You analyze payment failures and recovery decisions."),
            HumanMessage(content=prompt),
        ])
        return result.content
    except Exception as exc:
        return f"LLM analysis could not be completed: {exc}"
