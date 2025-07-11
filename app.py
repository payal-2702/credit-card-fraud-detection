# import streamlit as st
# # import pickle 
# import pandas as pd
# # from backend.alerts import send_alert

# st.set_page_config(page_title ='Credit Card Fraud Detector')
# st.markdown('### Enter transaction Details')

# # st.title("Credit Card Fraud Detection System")
# class DummyModel:
#     def predict(self,X):
#         return [1 if X.iloc[0]['amount']> 5000 else 0]
    
# model = DummyModel()
# # try:
# #     model = pickle.load(open('models/model.pkl','rb'))
# # except Exception as e:
# #     st.error(f'model loading failed:{e}')
# #     st.stop()

# # st.markdown('### Enter transaction details')

# # amount= st.number_input("Transaction Amount")
# # model= pickle.load(open('models/model.pkl','rb'))

# # st.set_page_config(page_title='Credit Card Fraud Detection')
# # st.title('credit card fraud detection system')

# # st.markdown('### Enter Transaction Details')

# amount= st.number_input("Transaction Amount", min_value=0.0)
# old_balance = st.number_input("Old Balance", min_value=0.0)
# new_balance= st.number_input ("New Balance", min_value=0.0)
# phone= st.text_input("Phone Number (+91...)")

# if st.button("Check Transaction"):
#     try:
#         data= pd.DataFrame([[amount, old_balance, new_balance]],
#                        columns=['amount','oldbalanceOrg','newbalanceOrig'])
#         prediction = model.predict(data)[0]
        
#         if prediction == 1:
#             st.error('Fraudelent Transaction Detected!')
#             send_alert(phone, "Alert: Fraud detected on your card.")
#         else:
#             st.success("Transaction is safe.")
#     except Exception as e:
#         st.error(f"prediction failed:{e}")
import streamlit as st
import time
import pandas as pd
import pickle
from backend.alerts import send_alert

st.set_page_config(page_title='Credit Card Fraud Detector')

st.markdown("### Enter transaction details")

st.title ("Credit card fraud detection")
st.write ("Enter following details")
amount=st.number_input("Transaction Amount", min_value=0.0)
card= st.selectbox("Card Type",["Visa","Master card","other"]) 
card_mapping = {'Visa':0,"Master card": 1,'other': 2}
card_num = card_mapping[card]
phone = st.text_input("Phone Number (+91....)")

if st.button("Submit"):
    try:
        model= pickle.load(open('models/make_demo_model.py','rb'))
    except:
        class DemoModel:
            def predict(self,X):
                amt, card= X.iloc[0]
                return [1 if amt > 5000 or card==2 else 0]
        model =  DemoModel()

    data = pd.DataFrame([[amount, card_num]], columns=["amount", 'card'])

    prediction = model.predict(data)[0]

    if prediction ==1:
        st.error("Fraudelent transaction detected!")
        send_alert(phone,"Alert: suspicious transaction on your card.")
    else:
        st.success("transaction is safe.")

   


# Title of the app
st.title('💳 Credit Card Fraud Simulator')
st.subheader("📊 Transaction Status Overview")

# Mock data
fraud_count = 23
legit_count = 77

data = {'Status': ['Fraud', 'Legitimate'], 'Count': [fraud_count, legit_count]}

# Pie chart with default colors
# fig = px.pie(
#     data,
#     names='Status',
#     values='Count',
#     title='Fraud vs Legitimate Transactions'
# )

# fig.update_traces(textposition='inside', textinfo='percent+label')

# st.plotly_chart(fig, use_container_width=True)



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
