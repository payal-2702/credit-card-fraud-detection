import streamlit as st

# Configure page
st.set_page_config(page_title="💳 Fraud Detection Simulator", layout="centered")

# Title
st.title("💳 Credit Card Fraud Simulator")

# Instructions
st.markdown("### 🛠️ How to Use the Simulator")
st.info("""
1. Enter the transaction amount.
2. Select the card type.
3. Enter Time (seconds from first transaction).
4. Select Location of transaction.
5. Select payment method.
6. Enter Customer deatils (Age, Transaction history)  
8. Click **Submit** to simulate the transaction.
9. The app will show whether it is likely to be fraudulent.
""")
# --- Input Section ---
st.header("🔧 Transaction Details")

amount = st.number_input("💵 Amount ($)", min_value=0.0, step=1.0)
time = st.number_input("⏱️ Time (seconds from first transaction)", min_value=0)
location = st.selectbox("📍 Location", ["Online", "In Store", "International"])
method = st.selectbox("💳 Payment Method", ["Credit", "Debit", "Mobile Payment", "Wire Transfer"])

st.header("🙋 Customer Details")

age = st.slider("Age", 18, 90, 30)
history = st.selectbox("📊 Customer History", ["Good", "Average", "Bad"])

# --- Fraud Detection Logic ---
def predict_fraud(amount, location, method, age, history):
    score = 0
    reasons = []

    if amount > 1000:
        score += 3
        reasons.append("High transaction amount: +3")
    elif amount > 500:
        score += 2
        reasons.append("Moderate transaction amount: +2")
    else:
        score += 1
        reasons.append("Low transaction amount: +1")

    if location == "International":
        score += 2
        reasons.append("International location: +2")
    elif location == "Online":
        score += 1
        reasons.append("Online transaction: +1")

    if method == "Wire Transfer":
        score += 2
        reasons.append("Payment by Wire Transfer: +2")
    elif method == "Credit":
        score += 1
        reasons.append("Payment by Credit: +1")

    if age < 25 or age > 70:
        score += 1
        reasons.append("Risky age range (<25 or >70): +1")

    if history == "Bad":
        score += 2
        reasons.append("Bad customer history: +2")
    elif history == "Average":
        score += 1
        reasons.append("Average customer history: +1")

    # Fraud threshold
    return ("Fraud", score, reasons) if score >= 6 else ("Legitimate", score, reasons)
if st.button("🔄 Reset Form"):
    st.session_state.reset = True
    st.rerun()  # 



# --- Result Section ---
if st.button("🚀 Simulate Transaction"):
    result, score, reasons = predict_fraud(amount, location, method, age, history)

    st.subheader("📋 Prediction Result")
    if result == "Fraud":
        st.error(f"🚨 Fraudulent Transaction Detected (Score: {score})")
    else:
        st.success(f"✅ Legitimate Transaction (Score: {score})")

    st.subheader("📌 Reason Breakdown")
    for r in reasons:
        st.write(f"- {r}")

    st.subheader("🧾 Transaction Summary")
    st.json({
        "Amount": amount,
        "Time": time,
        "Location": location,
        "Payment Method": method,
        "Age": age,
        "History": history,
        "Final Score": score,
        "Prediction": result
    })
