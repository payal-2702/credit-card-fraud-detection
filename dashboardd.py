import streamlit as st
st.title ("credit card fraud detection")
st.write ("Enter following details")
amount=st.number_input("Transaction Amount")
card= st.selectbox("Card Type",["Visa","Master card","other"]) # type: ignore
if st.button("Submit"):
   st.write("Transaction Submitted!")
