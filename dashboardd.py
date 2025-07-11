
import streamlit as st
import time
import plotly.express as px


st.title ("Credit card fraud detection")
st.write ("Enter following details")
amount=st.number_input("Transaction Amount")
card= st.selectbox("Card Type",["Visa","Master card","other"]) 
if st.button("Submit"):
   st.write("TRANSACTION SUBMITTED")


# Title of the app
st.title('💳 Credit Card Fraud Simulator')
st.subheader("📊 Transaction Status Overview")

# Mock data
fraud_count = 23
legit_count = 77

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



# Initialize session state to track the first transaction time if not already set
if 'first_transaction_time' not in st.session_state:
    st.session_state.first_transaction_time = time.time()

# Create a placeholder to display the real-time transaction time
time_placeholder = st.empty()

# Create a function to update the real-time transaction time
def update_transaction_time():
    # Calculate the elapsed time from the first transaction
    current_time = time.time() - st.session_state.first_transaction_time
    current_time_seconds = round(current_time, 2)  # Round for better readability

    # Update the placeholder with the new transaction time
    time_placeholder.subheader(f'Real-Time Transaction Time: {current_time_seconds} seconds')

    # Simulate a delay of 1 second to show the real-time update
    time.sleep(1)

# Display the current date and time in human-readable format
current_date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
st.write(f'Current Time: {current_date_time}')

# Button to simulate a new transaction
if st.button('New Transaction'):
    # Reset the first transaction time to the current time (for a new transaction)
    st.session_state.first_transaction_time = time.time()
    st.success("New Transaction Recorded!")  # Show success message

# Start updating the transaction time in real-time using st.empty() placeholder
while True:
    update_transaction_time()
    time.sleep(1)  # This delay ensures it updates every second
