PayRecoverAI

AI-powered payment failure analysis and revenue recovery assistant built for the Razorpay AI Builder Hackathon.

PayRecoverAI helps merchants understand why payments fail, identify root causes, estimate revenue at risk, and recommend recovery actions using transaction data and AI.

 Key Features
Payment Failure Analysis — analyzes failed transactions and identifies common failure reasons.
Root Cause Analysis — explains the likely reason behind a payment failure.
Recovery Strategy — recommends actions such as retrying, using an alternate payment method, or contacting the customer.
Revenue Recovery Dashboard — shows amount at risk, recovered amount, and recovery rate.
Failure Analytics — visualizes failures by reason and payment method.
Knowledge Graph — connects payment failure reasons with possible causes and recovery actions.
AI Payment Assistant — uses an LLM to provide contextual analysis.
CSV Upload — merchants can upload transaction data for analysis.
🛠️ Tech Stack
Python
Streamlit — web interface and dashboard
Groq API — LLM-powered analysis
Qwen — AI model used for analysis
Pandas — transaction-data processing
Plotly — data visualization
RAG — retrieval-augmented payment knowledge
Knowledge Graph — failure-cause and recovery relationships How It Works
Transaction CSV
      ↓
Data Processing
      ↓
Payment Failure Detection
      ↓
Root Cause Analysis
      ↓
Supporting Evidence
      ↓
Recovery Recommendation
      ↓
Revenue Recovery Insights
 Problem

Payment failures directly impact merchant revenue. Merchants often receive a failure code but don't get enough context to understand:

Why did the payment fail?
What is the actual root cause?
Which payments are worth recovering?
What action should be taken next?
 Solution

PayRecoverAI converts raw payment failure data into actionable recovery intelligence, helping merchants prioritize failed payments and choose appropriate recovery actions.

Demo

The application provides:

Transaction count
Failed payment count
Amount at risk
Recovered amount
Recovery rate
Failure-reason analytics
Payment-method analytics
Individual payment root-cause analysis
AI-powered recovery recommendations
⚠️Disclaimer

The hackathon demo uses controlled transaction data. In a production system, recovery outcomes would be connected to actual payment-gateway transaction events/webhooks.

 Run Locally
git clone https://github.com/tahaali84/PayRecoverAI.git
cd PayRecoverAI

Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Add your Groq API key through Streamlit secrets:

.streamlit/secrets.toml

Then run:

streamlit run app.py
