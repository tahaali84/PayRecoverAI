# PayRecoverAI

AI-powered payment failure analysis and revenue recovery assistant built for the **Razorpay AI Builder Hackathon 2026**.

## Overview

PayRecoverAI helps merchants analyze failed payments, identify likely root causes, understand revenue at risk, and determine appropriate recovery actions.

The system converts transaction data into actionable payment recovery insights through analytics, rule-based reasoning, RAG, knowledge graphs, and LLM-powered analysis.

## Features

- **Payment Failure Analysis**  
  Analyze failed transactions and identify common failure reasons.

- **Root Cause Analysis**  
  Determine the likely cause behind a payment failure with supporting evidence.

- **Recovery Strategy**  
  Recommend suitable recovery actions such as retrying the payment or suggesting an alternate payment method.

- **Revenue Recovery Dashboard**  
  Track transactions, failed payments, amount at risk, recovered amount, and recovery rate.

- **Payment Analytics**  
  Visualize payment failures by failure reason and payment method.

- **Knowledge Graph**  
  Connect payment failure reasons with possible causes and recovery actions.

- **AI Payment Assistant**  
  Use an LLM to provide contextual analysis and recovery recommendations.

- **CSV Transaction Upload**  
  Upload payment transaction data for analysis.

## How It Works

```text
Transaction Data
       ↓
Data Processing
       ↓
Payment Failure Analysis
       ↓
Root Cause Identification
       ↓
Evidence Retrieval
       ↓
Recovery Recommendation
       ↓
Revenue Recovery Insights


                         PayRecoverAI
                              │
                ┌─────────────┴─────────────┐
                │                           │
         Transaction Data              User Input
                │                           │
                ↓                           ↓
         Data Processing             Streamlit UI
                │                           │
                └─────────────┬─────────────┘
                              ↓
                   Payment Intelligence
                              │
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
        Root Cause          RAG          Knowledge Graph
          Analysis        Retrieval
              │               │               │
              └───────────────┼───────────────┘
                              ↓
                         Groq + Qwen
                              │
                              ↓
                  Recovery Recommendation
                              │
                              ↓
                    Merchant Dashboard
