import streamlit as st
import time
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="💳 Transaction Defender ", layout="centered")

# --- Sidebar Navigation ---
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Choose Page", ["Dashboard", "Simulator"])

# --- DASHBOARD PAGE ---
if page == "Dashboard":
    st.title(" Transaction Defender Dashboard")
    st.subheader("📊 Transaction Status Overview")

    if 'fraud_count' not in st.session_state:
        st.session_state.fraud_count = 0
    if 'legit_count' not in st.session_state:
        st.session_state.legit_count = 0

    fraud_count = st.session_state.fraud_count
    legit_count = st.session_state.legit_count

    data = {'Status': ['Fraud', 'Legitimate'], 'Count': [fraud_count, legit_count]}

    # Pie chart with default colors
    fig = px.pie(
        data,
        names='Status',
        values='Count',
        title='Fraud vs Legitimate Transactions'
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)

    # Initialize session state to track the first transaction time
    if 'first_transaction_time' not in st.session_state:
        st.session_state.first_transaction_time = time.time()

    # Create a placeholder to display the real-time transaction time
    time_placeholder = st.empty()

    # Function to update the timer
    def update_transaction_time():
        current_time = time.time() - st.session_state.first_transaction_time
        current_time_seconds = round(current_time, 2)
        time_placeholder.subheader(f'Real-Time Transaction Time: {current_time_seconds} seconds')
        time.sleep(1)

    # Display current date & time
    current_date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    st.write(f'Current Time: {current_date_time}')

    # Button to simulate new transaction
    if st.button('New Transaction'):
        st.session_state.first_transaction_time = time.time()
        st.success("New Transaction Recorded!")

    # Start timer loop
    while True:
        update_transaction_time()
        time.sleep(1)

# --- SIMULATOR PAGE ---
elif page == "Simulator":
    st.title("Credit card fraud simulator")

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
    mobileno= st.number_input("Enter your mobile number")

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

        return ("Fraud", score, reasons) if score >= 6 else ("Legitimate", score, reasons)

    if st.button("🔄 Reset Form"):
        st.session_state.reset = True
        st.rerun()

    # --- Result Section ---
    if st.button("🚀 Simulate Transaction"):
        result, score, reasons = predict_fraud(amount, location, method, age, history)

        st.subheader("📋 Prediction Result")
        if result == "Fraud":
            st.error(f"🚨 Fraudulent Transaction Detected (Score: {score})")
            st.session_state.fraud_count += 1
        else:
            st.success(f"✅ Legitimate Transaction (Score: {score})")
            st.session_state.legit_count += 1

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
