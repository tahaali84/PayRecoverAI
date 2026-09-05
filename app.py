import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from ingestion.doc_loader import load_transactions, validate_transactions
from features.root_cause import analyze_failure
from features.recovery import build_recovery_plan, recovery_summary
from features.knowledge_graph import build_payment_graph
from utils.graph_visualizer import graph_to_html
from rag.rag_chain import answer_payment_question

load_dotenv()

st.set_page_config(page_title="PayRecover AI", page_icon="💳", layout="wide")

st.title(" PayRecover AI")
st.caption("AI-powered payment failure analysis and revenue recovery assistant")

with st.sidebar:
    st.header("Payment Intelligence")
    groq_key = st.text_input("Groq API Key", type="password")
    uploaded = st.file_uploader(
        "Upload payment transaction CSV",
        type=["csv"],
    )
    st.caption("Demo: PayRecover_final_transactions.csv")

if uploaded:
    df = load_transactions(uploaded)
else:
    default_path = os.path.join(os.path.dirname(__file__), "data", "PayRecover_final_transactions.csv")
    if os.path.exists(default_path):
        df = load_transactions(default_path)
    else:
        st.info("Upload a payment transaction CSV to begin.")
        st.stop()

missing = validate_transactions(df)
if missing:
    st.error("Missing required columns: " + ", ".join(missing))
    st.stop()

failed = df[df["status"].eq("FAILED")].copy()
amount_at_risk = failed["amount_inr"].sum()
recovered = df["recovered_amount_inr"].sum()
recovery_rate = recovered / amount_at_risk * 100 if amount_at_risk else 0

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Transactions", len(df))
c2.metric("Failed Payments", len(failed))
c3.metric("Amount at Risk", f"₹{amount_at_risk:,.0f}")
c4.metric("Recovered", f"₹{recovered:,.0f}")
c5.metric("Recovery Rate", f"{recovery_rate:.1f}%")

st.divider()

mode = st.radio(
    "Module",
    ["Overview", "Payment Failure RCA", "Recovery Strategy", "Knowledge Graph", "Payment Assistant", "Transactions"],
    horizontal=True,
)

if mode == "Overview":
    left, right = st.columns(2)
    with left:
        st.subheader("Failure Reasons")
        counts = failed["failure_reason"].replace("", "UNKNOWN").value_counts()
        st.bar_chart(counts)
    with right:
        st.subheader("Payment Methods")
        st.bar_chart(df["payment_method"].value_counts())

    st.subheader("Recovery by Failure Reason")
    st.dataframe(recovery_summary(df), use_container_width=True, hide_index=True)

elif mode == "Payment Failure RCA":
    st.subheader("🔎 Payment Failure Root Cause Analysis")
    if failed.empty:
        st.success("No failed payments.")
        st.stop()

    tx_id = st.selectbox("Select failed transaction", failed["transaction_id"].tolist())
    tx = failed.loc[failed["transaction_id"].eq(tx_id)].iloc[0]

    result = analyze_failure(tx)

    a, b, c, d = st.columns(4)
    a.metric("Amount", f"₹{tx.amount_inr:,.0f}")
    b.metric("Attempts", int(tx.attempts))
    c.metric("Failure", tx.failure_reason)
    d.metric("Priority", result["priority"])

    st.markdown("### Root Cause")
    st.write(result["root_cause"])
    st.markdown("### Evidence")
    st.write(result["evidence"])
    st.markdown("### Recommended Action")
    st.info(result["action"])

    if groq_key:
        if st.button("Run LLM Analysis", type="primary"):
            with st.spinner("Analyzing payment evidence..."):
                st.write(answer_payment_question(
                    f"Analyze transaction {tx_id} and explain the root cause and safest recovery action.",
                    df, groq_key, selected_transaction=tx
                ))
    else:
        st.caption("Add a Groq API key to enable LLM reasoning.")

elif mode == "Recovery Strategy":
    st.subheader("🎯 Recovery Strategy")
    plan = build_recovery_plan(failed)
    st.dataframe(plan, use_container_width=True, hide_index=True)
    st.warning("Recovery retries are intentionally bounded. Repeated issuer declines should move to an alternate payment method or escalation.")

elif mode == "Knowledge Graph":
    st.subheader("🕸️ Payment Knowledge Graph")
    tx_id = st.selectbox("Transaction", df["transaction_id"].tolist())
    tx = df.loc[df["transaction_id"].eq(tx_id)].iloc[0]
    graph = build_payment_graph(tx)
    html = graph_to_html(graph)
    st.components.v1.html(html, height=600, scrolling=True)

elif mode == "Payment Assistant":
    st.subheader("🤖 Payment Intelligence Assistant")
    question = st.text_input("Ask about the transaction data")
    if question:
        if groq_key:
            with st.spinner("Analyzing..."):
                st.write(answer_payment_question(question, df, groq_key))
        else:
            st.info("Add your Groq API key to use the Payment Assistant.")

elif mode == "Transactions":
    st.subheader("🔍 Transaction Explorer")
    statuses = st.multiselect("Status", sorted(df.status.unique()), default=sorted(df.status.unique()))
    methods = st.multiselect("Payment Method", sorted(df.payment_method.unique()), default=sorted(df.payment_method.unique()))
    filtered = df[df.status.isin(statuses) & df.payment_method.isin(methods)]
    st.dataframe(filtered, use_container_width=True, hide_index=True)

